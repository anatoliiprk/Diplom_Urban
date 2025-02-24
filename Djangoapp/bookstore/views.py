from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from .models import Profile, Book, Basket


# Create your views here.



def main(request):
    title = 'Книжный магазин'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'main.html', context)


def catalog(request):
    title = 'Каталог'
    text = 'Книги'
    books = Book.objects.all()
    context = {
        'title': title,
        'text': text,
        'books': books
    }
    return render(request, 'books.html', context)


def basket_page(request):
    if not request.user.is_authenticated:
        return render(request, 'basket.html')
    basket, created = Basket.objects.get_or_create(user=request.user)
    books = basket.books.all()
    total_price = sum(book.cost for book in books)
    return render(request, 'basket.html', {'books': books, 'total_price': total_price})


def add_to_basket(request, book_id):
    if not request.user.is_authenticated:
        return redirect('login')
    book = get_object_or_404(Book, id=book_id)
    basket, created = Basket.objects.get_or_create(user=request.user)
    basket.books.add(book)
    return redirect('basket')


def delete_from_basket(request, book_id):
    if not request.user.is_authenticated:
        return redirect('login')
    book = get_object_or_404(Book, id=book_id)
    basket = Basket.objects.get(user=request.user)
    basket.books.remove(book)
    return redirect('basket')


def sign_in(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, phone_number=form.cleaned_data.get('phone_number'))
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'sign_in.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('main')
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('main')
