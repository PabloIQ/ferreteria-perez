from django import forms
import django
from django.contrib.auth import models
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class RegistrarForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'formulario__input',
            'required': ''
        })
        self.fields['email'].widget.attrs.update({
            'class': 'formulario__input',
            'required': ''
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'formulario__input',
            'required': ''
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'formulario__input',
            'required': ''
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'formulario__input',
            'required': ''
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'formulario__input',
            'required': ''
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']