from fastapi import FastAPI
import uvicorn
from passlib.context import CryptContext
from database import engine, metadata, database
import models
from fastapi import Request, Form, status
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

metadata.create_all(engine)


@app.on_event("startup")
async def startup():
    await database.connect()
    # Добавление начальных данных о книгах
    query = models.books.select()
    books = await database.fetch_all(query)
    if not books:
        books_list = [
            {"title": "Варяг", "author": "Мазин А.В.", "genre": "Историческая фантастика", "cost": 500},
            {"title": "Место для битвы", "author": "Мазин А.В.", "genre": "Историческая фантастика", "cost": 400},
            {"title": "Князь", "author": "Мазин А.В.", "genre": "Историческая фантастика", "cost": 600},
            {"title": "Кредо Виканки. Знаки и знамения", "author": "Мара Вульф", "genre": "Фэнтези", "cost": 850},
            {"title": "Кредо Виканки. Вина и грехи", "author": "Мара Вульф", "genre": "Фэнтези", "cost": 900},
            {"title": "Кредо Виканки. Месть и огонь", "author": "Мара Вульф", "genre": "Фэнтези", "cost": 1050},
        ]
        query = models.books.insert()
        await database.execute_many(query, books_list)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# Здесь будут маршруты (routes)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

templates = Jinja2Templates(directory="templates")


@app.get("/sign-in", response_class=HTMLResponse)
async def sign_in(request: Request):
    return templates.TemplateResponse("sign_in.html", {"request": request})


@app.post("/sign-in")
async def sign_in_post(request: Request,
                       username: str = Form(..., max_length=30),
                       password: str = Form(...),
                       password_confirm: str = Form(...),
                       age: int = Form(...)):
    if len(password) < 8:
        return templates.TemplateResponse("sign_in.html",
                                          {"request": request, "error": "Пароль должен быть не менее 8 символов"})
    if password != password_confirm:
        return templates.TemplateResponse("sign_in.html", {"request": request, "error": "Пароли не совпадают"})

    query = models.users.select().where(models.users.c.username == username)
    existing_user = await database.fetch_one(query)
    if existing_user:
        return templates.TemplateResponse("sign_in.html", {"request": request, "error": "Пользователь уже существует"})

    hashed_password = get_password_hash(password)
    query = models.users.insert().values(username=username, password_hash=hashed_password, age=age)
    await database.execute(query)
    return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login_post(request: Request, username: str = Form(...), password: str = Form(...)):
    query = models.users.select().where(models.users.c.username == username)
    user = await database.fetch_one(query)
    if not user or not verify_password(password, user["password_hash"]):
        return templates.TemplateResponse("login.html", {"request": request, "error": "Неверный логин или пароль"})
    request.session["user"] = {"id": user["id"], "username": user["username"]}
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)


@app.get("/logout")
async def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    user = request.session.get("user")
    return templates.TemplateResponse("main.html", {"request": request, "user": user})


@app.get("/catalog", response_class=HTMLResponse)
async def books_page(request: Request):
    query = models.books.select()
    book_list = await database.fetch_all(query)
    user = request.session.get("user")
    return templates.TemplateResponse("books.html", {"request": request, "books": book_list, "user": user})


@app.post("/books/add-to-basket/{book_id}")
async def add_to_basket(request: Request, book_id: int):
    user = request.session.get("user")
    if not user:
        return RedirectResponse(url="/catalog", status_code=status.HTTP_302_FOUND)
    query = models.basket.insert().values(user_id=user["id"], book_id=book_id)
    await database.execute(query)
    return RedirectResponse(url="/basket", status_code=status.HTTP_302_FOUND)


@app.get("/basket", response_class=HTMLResponse)
async def cart(request: Request):
    user = request.session.get("user")
    if not user:
        return templates.TemplateResponse("basket.html", {"request": request,
                                                          "message": "Вы не авторизованы. Пожалуйста, войдите в аккаунт"
                                                                     "или зарегистрируйтесь"})

    query = """
        SELECT books.id, books.title, books.author, books.genre, books.cost
        FROM basket
        JOIN books ON basket.book_id = books.id
        WHERE basket.user_id = :user_id
    """
    items = await database.fetch_all(query=query, values={"user_id": user["id"]})
    total = sum(item["cost"] for item in items)

    return templates.TemplateResponse("basket.html", {"request": request, "items": items, "total": total, "user": user})


@app.post("/basket/delete/{book_id}")
async def delete_from_basket(request: Request, book_id: int):
    user = request.session.get("user")
    if not user:
        return RedirectResponse(url="/basket", status_code=status.HTTP_302_FOUND)
    query = models.basket.delete().where(models.basket.c.user_id == user["id"], models.basket.c.book_id == book_id)
    await database.execute(query)
    return RedirectResponse(url="/basket", status_code=status.HTTP_302_FOUND)


app.mount("/static", StaticFiles(directory="static"), name="static")
