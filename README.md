

# Дипломная работа 
на тему: 
**“Анализ и сравнение написания web-приложений с использованием разных фреймворков”** 




Выполнил: Карпов Анатолий Викторович


----
 

# **Содержание** 

## Введение

### Обоснование выбранной темы

### Цели и задачи исследования

## Понятия и определения

## Ключевые особенности фреймворков

## Разработка веб приложений Django, Flask иFastAPI 

### Пример работы на Django

### Пример работы на Flask

### Пример работы на FastAPI

## Анализ работы на Django, Flask и FastAPI

## Приложение 1. Пример файловой структуры

## Приложение 2. Список необходимых библиотек
 
----

# **Введение.**

Проект посвящен сравнительному анализу различных фреймворков для разработки веб-приложений, таких как Django, FastAPI и Flask. Основное внимание уделяется преимуществам и недостаткам использования фреймворков, а также возможности разработки приложений без них. Исследование включает в себя оценку информативности, удобства, скорости разработки и поддержки со стороны сообщества. Это позволит разработчикам сделать осознанный выбор в зависимости от своих потребностей и квалификации, а также выявить ключевые аспекты, которые влияют на процесс разработки.
 

 ----

# **Цели и задачи исследования**

Цель исследования: выявить наиболее удобный и качественный фреймворк для разработки сайтов и веб-приложений, либо же определить, для каких задач больше подходят наиболее известные фреймворки.

Задачи исследования:

определение наиболее популярных и востребованных фреймворков;

выявление ключевых особенностей выбранных фреймворков;

разработка веб-приложения на каждом из них на тему "Магазин приложений"

сравнение приложений.

----
## **Понятия и опрделения** 

Веб-приложение – программное приложение, работающее на веб-сервере через браузер.

Бэкенд (backend) – серверная часть веб-приложения, обрабатывающая запросы от клиента, выполняющая логику приложения и взаимодействующая с базой данных.

Фронтенд (frontend) – клиентская часть веб-приложения, взаимодействующая непосредственно с пользователем, отвечающая за отображение данных и предоставления пользователю интерфейса взаимодействия с приложением.

Веб-фреймворк (Web-framework) – набор инструментов для написания бэкенда веб-приложения.

ORM (Object-Relational Mapping) – технология взаимодействия с базой данных через объектно-ориентированный интерфейс, скрывая детали SQL-запросов. 


----
## **Ключевые особенности фреймворков** 

Разберём ключевые особенности каждых из наиболее востребованных фреймворков.

### Django

Django следует философии "batteries-included" (все необходимые компоненты "из коробки"), что означает, что он предоставляет обширный набор встроенных инструментов и функций для разработки веб-приложений. Это включает в себя:
 
автоматически создаваемая административная панель, позволяющая управлять данными вашего приложения без написания кода;

инструмент для взаимодействия с базами данных, позволяющий работать с данными как с объектами Python;
	
механизм для валидации и обработки пользовательских вводов;
	
модели, обеспечивающие легкость определения структуры базы данных с использованием Python-классов.

В архитектурном плане Django использует паттерн MVT (Model-View-Template), что позволяет разделить логику приложения на три взаимосвязанных компонента:

Model – модель, отвечающая за структуру и поведение данных;

View – представление, обрабатывающая логику отображения данных;

Template – шаблон, отвечающий за оформление и отображение пользовательского интерфейса.

### FastAPI

FastAPI — это относительно новый, высокопроизводительный веб-фреймворк для создания API на языке Python. Он разработан для обеспечения высокой скорости разработки и работы приложений, поддерживает асинхронное программирование и соответствует современным стандартам API, таким как OpenAPI и JSON Schema. Ключевыми особенностями FastAPI являются:
	
высокая производительность, так как фреймворк основан на Starlette и Pydantic, а также использует асинхронное программирование, что позволяет обрабатывать множество запросов одновременно, не блокируя сервер;
	
автоматическая генерация документация на основе аннотации типов Python, которая доступна в интерактивной форме через Swagger UI и ReDoc:
	
высокая скорость разработки с минимальным количеством кода.

### Flask

Flask — это легковесный веб-фреймворк для Python, который известен своей простотой и гибкостью. Он следует принципу минимализма и предоставляет разработчикам базовые инструменты для создания веб-приложений, оставляя возможность добавлять нужную функциональность с помощью расширений. Ключевыми особенностями Flask являются:

легковесность за счёт минимально набора инструментов для создания веб приложений;

фреймворк не накладывает ограничения на архитектуру приложения, благодаря чему разработчик может выстроить архитектуру так, как требуется ему;

поддержка множество сторонних расширений, таких как интеграция с базами данных, системами аутентификации и обработкой форм;

поддержка шаблонов Jinja2 для создания HTML-шаблонов.


----

# **Примеры работы программы на Django, FastAPI и Flask** 

## **Пример работы на Django** 

Перед началом разработки приложения на Django, его нужно установить. Делается это, с помощью консольной команды “pip install Django”. Далее, чтобы начать разработку проекта, в консоли нужно прописать “django-admin startproject <имя файла>” (рис. 1.1) и (рис. 1.2). 

![Django](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Django/1.JPG)

(рис. 1.1) 

![Django](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Django/2.JPG)

(рис. 1.2) 

После этого необходимо создать приложение в проекте с помощью команды «python manage.py startapp <название приложения>». Перед тем, как выполнять данную команду необходимо перейти в директорию проекта в терминале с помощью команды «cd <название проекта>». После выполнения команд будет создана директория с приложением, в которой находятся инструменты для настройки отображения страниц, взаимодействия с базой данных и аутентификации пользователей. (рис. 1.3). 

![Django](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Django/3.JPG)

(рис. 1.3) 

Далее к проекту необходимо подключить и само приложение в файле «settings.py», иначе при запуске сервера будет ошибка, либо ничего не будет отображено (рис. 1.4). 

![Django](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Django/4.JPG)

(рис. 1.4) 

После этого, для того, чтобы взаимодействовать с отображениями страниц в этом в том же файле «settings.py» нужно спуститься в TEMPLATES, а конкретнее в листе “DIRS” и прописать вашу папку с шаблонами например: “[BASE_DIR / ‘templates’]” (рис. 1.5). 

![Django](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Django/5.JPG)

(рис. 1.5) 

Чтобы настроить отображение на сайте, необходимо использовать файл «views.py». В ней пишутся функции и классы, в которых настраивается логика взаимодействия с сервером (рис. 1.6.1), (рис. 1.6.2), (рис. 1.6.3).

main - отображает главную страницу сайта
catalog - отображает страницу магазина
add_to_basket - добавляет книгу в корзину пользователя
delete_from_basket - удаляет книгу из корзины пользователя
basket_page - отображает содержимое корзины пользователя
sign_in - обрабатывает регистрацию нового пользователя
login_page - обрабатывает вход пользователя
logout_page - обрабатывает выход пользователя

![Django](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Django/6.1.JPG)

(рис. 1.6.1)

![Django](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Django/6.2.JPG)

(рис. 1.6.2)

![Django](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Django/6.3.JPG)

(рис. 1.6.3)

Для создания моделей необходимо пользоваться файлом «models.py», в котором будут создаваться таблицы (рис. 1.7).

![Django](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Django/7.JPG)

(рис. 1.7)

Чтобы настроить взаимодействие с базой данных, для начала нужно выполнить команды «python manage.py makemigrations» для проверки не сохранённых связей таблиц и «python manage.py migrate» для сохранения этих связей. Данные команды необходимо использовать каждый раз при добавлении новых моделей (таблиц) в ваше приложение

После этого мы создаем суперпользователя (для админки) выполнив команду «python manage.py createsuperuser» и в файле admin.py зарегестрируем модели, чтобы потом с помощью администратора добавлять нужные нам книги, где будут указаны их названия, имена авторов и цена (рис. 1.8). 

![Django](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Django/8.JPG)

(рис. 1.8)

Теперь переходим в папку urls.py в ней нам нужно прописать все пути, которые мы хотим сделать с помощью path (рис. 1.9). 

![Django](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Django/9.JPG)

(рис. 1.9) 

Чтобы запустить проект осталось прописать в консоли команду “python manage.py runserver”(рис. 1.10).

![Django](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Django/10.JPG)

(рис. 1.10)

Переходим по ссылке http://127.0.0.1:8000 на главную страницу нашего сайта и чтобы добавить на сайт нужные книги, мы добавляем к нашему адресу http://127.0.0.1:8000/admin/ и в разделе bookstore/book нажимаем кнопку "добавить" и записываем нужные нам параметры (рис. 1.11.1), (рис. 1.11.2). 

![Django](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/HTML/2.JPG)

(рис. 1.11.1)

![Django](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Django/11.JPG)

(рис. 1.11.2)

## **Пример работы на FastAPI** 

Перед началом работы с FastAPI нужно его установить. Сначала также устанавливаем FastAPI “pip install fastapi” и создаём директорию с файлом(рис. 2.1). 

![FastAPI](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/FastAPI/1.JPG)

(рис. 2.1) 

Потом мы создаем необходимые для работы папки и файлы, такие как templates для взаимодействия с отображениями страниц, database.py для работы с базой данных проекта, main.py для запуска проекта, models.py для описания структуры базы данных, schemas.py для проверки данных и работы с ними (рис. 2.2) 

![FastAPI](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/FastAPI/2.JPG)

(рис. 2.2)

В файле database.py пишем код для использования библиотек "Databases" и "SQLAlchemy"(рис. 2.3) 

![FastAPI](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/FastAPI/3.JPG)

(рис. 2.3) 

После этого в файле models.py cоздаем описания структуры базы данных для работы с ними (так называемая декларация схемы) (рис. 2.4). 

![FastAPI](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/FastAPI/4.JPG)

(рис. 2.4)

В файле schemas.py с помощью библиотеки "Pydantic" создаем модели данных, которые проверяют входные данные на соответсвие заданным типам и структуре (рис. 2.5).

![FastAPI](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/FastAPI/5.JPG)
 
(рис. 2.5)

В файле main.py прописываем шаблоны для настройки проекта и отображения их на сайте (рис. 2.6).

![FastAPI](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/FastAPI/6.JPG)

(рис. 2.6)

Далее создаем такой же templates как и в Django, но этот будет содержать Jinja2Templates с указанным путём в папку с шаблонами (рис. 2.7.1),(рис. 2.7.2).

![FastAPI](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/FastAPI/7.1.JPG)

(рис. 2.7.1)

![FastAPI](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/FastAPI/7.2.JPG)

(рис. 2.7.2)

## **Пример работы на Flask** 

Для того чтобы начать работу на Flask нужно установить его с помощью консольной команды “pip install Flask, Flask_sqlalchemy Flask_login ”.(рис. 3.1) 

![flask](https://github.com/anatoliiprk/Diplom_Urban/tree/main/image/Flask)

(рис. 3.1) 



Далее для реализации проекта необходимо создать файлы (рис. 3.2):
app.py - для запуска проекта
init_db.py - для инициализации базы данных
models.py - для создания моделей
templates.py - для взаимодействия с отображениями страниц

![flask](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Flask/2.JPG)

(рис. 3.2) 

В основном файле app.py настраиваем приложение (рис 3.3.1), (рис 3.3.2), (рис 3.3.3) 

![flask](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Flask/3.1.JPG)

(рис. 3.3.1)

![flask](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Flask/3.2.JPG)

(рис. 3.3.2)

![flask](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Flask/3.3.JPG)

(рис. 3.3.3)

Далее с помощью файла models.py представлена реализация базовой структуры базы данных для веб-приложения с использованием Flask, SQLAlchemy и Flask-Login. В данном коде создаются модели для работы с книгами, пользователями и корзиной покупок(рис. 3.4).

![flask](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Flask/4.JPG)

(рис. 3.4)

После этого с помощью файла init_db.py инициализируем базу данных и добавляем начальные данные(рис. 3.5).

![flask](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/Flask/5.JPG)

(рис. 3.5)

## **Шаблоны HTML** 

Шаблон menu необходим для отображения панели навигации и явлется базовым для других шаблонов (рис. 4.1).

![HTML](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/HTML/1.JPG)

(рис. 4.1)

Второй шаблон main отображает главную страницу сайта (рис. 4.2).

![HTML](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/HTML/2.JPG)

(рис. 4.2)

Третий шаблон books служит для отображения каталога книг и их покупки (рис. 4.3). 

![HTML](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/HTML/3.JPG)

(рис. 4.3)

Так же есть шаблон basket, отвечающий за отображение страницы с корзиной пользователя (рис. 4.4)

![HTML](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/HTML/4.JPG)

(рис.4.4) 

В шаблоне sign_in любой пользователь может зарегестрироваться, чтобы иметь возможность покупать книги (рис. 4.5).

![HTML](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/HTML/5.JPG)

(рис. 4.5)

В шаблоне login зарегестрированный пользователь может вернуться в свой аккаунт и продолжать покупки (рис. 4.6).

![HTML](https://github.com/anatoliiprk/Diplom_Urban/blob/main/image/HTML/6.JPG)

(рис. 4.6)

----

# Анализ работы на Django, Flask и FastAPI

После разработки одного и того же сайта на трёх разных фреймворках и анализа получившихся проектов можно прийти к выводу, что разработка на каждом из них хоть и схожа, но имеет отличительные особенности.

### Django

Разработка на Django подразумевает очень строгие требования к иерархии и архитектуре проекта, но за счёт этого разработчик меньше задумывается о подключении тех или иных приложений к проекту, настройки связи с базой данных, а также меньше беспокоится о защите. Благодаря строгости в архитектуре, большинство моментов по связи отдельных компонентов программы берёт на себя сам фреймворк. Если понять, как именно должны располагаться файлы, то разработка на Django становится не сложной и понятной. Минусом же Django является его же плюс: новичку будет достаточно сложно разобраться в том, как правильно взаимодействовать с файлами фреймворка.

### FastAPI

Разработка на FastAPI – очень простой и незамысловатый процесс, т.к. в отличии от Django фреймворк не накладывает строгих ограничений на архитектуру проекта, а также не имеет предустановленных инструментов для взаимодействия с базой данных и защиты. FastAPI – пустой холст для разработчика: на данном фреймворке разработчик сможет реализовать практически любую задумку именно так, как он хочет. Также, несомненным плюсом данного фреймворка является разработка посредством асинхронных функций, что делает его крайне быстрым. Ещё один немаловажный плюс – использование декораторов запросов. Данная особенность делает разработку отображений более систематизированной, понятной и удобочитаемой. Название отображает самое явное назначение этого фреймворка: он идеально подходит для разработки различных API вашего сервиса. 

Главным минусом является отсутствие предустановленных библиотек для взаимодействия с базами данных и защиты данных (работ с формами). Эта особенность позволяет FastAPI быть менее требовательным к ресурсам сервера, но приводит к сложности со связью между компонентами. Несмотря на то, что уже давно выведен каноничный набор FastAPI, SQLAlchemy и Alembic, возникают сложности с миграциями и взаимодействием с базами данных.

### Flask

Flask является чем-то средним между Django и FastAPI. В данном фреймворке «с коробки» также предоставлен достаточно малый набор инструментов для разработки приложения. Но, также, как и FastAPI, это дает преимущество перед Django в плане ресурсоемкости. И также, как у FastAPI, Flask не предъявляет очень строгих требований к архитектуре проекта. Но в отличии от FastAPI, данный фреймворк имеет свои аналоги-дополнения популярным библиотекам для взаимодействия с базами данных и прочим. Благодаря этим дополнениям, настройка связи происходит достаточно легко и интуитивно: установил дополнение, подключил его к приложению с помощью метода «init_app» - готово! Если возникает необходимость что-либо сделать в терминале, то на помощь приходит ключевое слово «flask», в которую сразу же добавляются команды дополнений. Также, в данном фреймворке по аналогии с FastAPI используются декораторы, что делает разработку систематизированной и удобной для восприятия. 


----

# **Приложение 1. Пример файловой структуры проекта** 

DiplomUrban

| .venv

|  Djangoapp 

|  |  bookstore

|  |  |  migrations

|  |  |  |  0001_initial.py

|  |  |  |  __init__.py

|  |  |  __init__.py

|  |  |  admin.py

|  |  |  apps.py

|  |  |  forms.py

|  |  |  models.py

|  |  |  tests.py

|  |  |  views.py

|  |  static

|  |  |  css

|  |  |  |  style

|  |  Djangoapp

|  |  |  __init__.py 

|  |  |  asgi.py

|  |  |  settings.py

|  |  |  urls.py

|  |  |  wsgi.py 

|  |  templates 

|  |  |  basket.html 

|  |  |  books.html 

|  |  |  login.html

|  |  |  main.html 

|  |  |  menu.html 

|  |  |  sign_in.html 

|  |  db.sqlite3 

|  |  manage.py 

----
|  FastAPI 

|  |  migrations

|  |  |  versions

|  |  |  |  069b0dc85167_initial_migration.py

|  |  |  env.py

|  |  |  README

|  |  |  script.py.mako

|  |  static

|  |  |  css

|  |  |  |  style

|  |  templates 

|  |  |  basket.html 

|  |  | books.html 

|  |  |  login.html

|  |  |  main.html 

|  |  |  menu.html 

|  |  |  sign_in.html 

|  |  alembic.ini

|  |  database.py

|  |  db.sqlite3 

|  |  main.py

|  |  models.py

|  |  schemas.py

----
|  Flask 

|  |  instance

|  |  |  db.sqlite3

|  |  migrations

|  |  |  versions

|  |  |  |  8767aa5ddbea_update_books.py

|  |  |  alembic.ini

|  |  |  env.py

|  |  |  README

|  |  |  script.py.mako

|  |  static

|  |  |  css

|  |  |  |  style

|  |  templates 

|  |  |  basket.html 

|  |  |  books.html 

|  |  |  login.html

|  |  |  main.html 

|  |  |  menu.html 

|  |  |  sign_in.html 

|  |  app.py

|  |  init_db.py

|  |  models.py
 
----
# **Приложение 2. Список необходимых библиотек**

aiosqlite==0.20.0
alembic==1.14.1
annotated-types==0.7.0
anyio==4.8.0
asgiref==3.8.1
blinker==1.9.0
click==8.1.8
colorama==0.4.6
databases==0.9.0
Django==5.1.5
fastapi==0.115.6
Flask==3.1.0
Flask-Login==0.6.3
Flask-Migrate==4.1.0
Flask-Script==2.0.6
Flask-SQLAlchemy==3.1.1
greenlet==3.1.1
h11==0.14.0
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.5
Mako==1.3.8
MarkupSafe==3.0.2
passlib==1.7.4
pydantic==2.10.5
pydantic_core==2.27.2
python-multipart==0.0.20
sniffio==1.3.1
SQLAlchemy==2.0.37
sqlparse==0.5.3
starlette==0.41.3
typing_extensions==4.12.2
tzdata==2024.2
uvicorn==0.34.0
Werkzeug==3.1.3
