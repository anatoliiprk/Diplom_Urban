from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    buyer = models.ManyToManyField(User, related_name='books')

    def __str__(self):
        return self.title


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)