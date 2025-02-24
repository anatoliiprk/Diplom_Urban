"""
URL configuration for Djangoapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookstore.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('catalog/', catalog, name='catalog'),
    path('basket/', basket_page, name='basket'),
    path('add_to_basket/<int:book_id>/', add_to_basket, name='add_to_basket'),
    path('delete_from_basket/<int:book_id>/', delete_from_basket, name='delete_from_basket'),
    path('sign-in/', sign_in, name='sign-in'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]
