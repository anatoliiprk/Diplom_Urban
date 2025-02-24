from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, help_text='Номер телефона в формате +7-ХХХ-ХХХ-ХХХХ',
                                   label='Номер телефона')

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email', 'password1', 'password2',)
