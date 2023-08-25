from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")
        field_classes = {"username": UsernameField}

        

