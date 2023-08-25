from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django import forms
import re

# For main-page response
from app_lesson_4.views import index

MAIN_PAGE_RESPONSE = index

TEML_ROOT = "app_authorization/"

# Create your views here.


# def advertisement_post(request):
#     return render(request, "app_lesson_4"+"register.html")

def register(request):
    context = {}
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy("profile"))

        print(form.errors.as_text())
        context["error"] = form.errors.as_text().replace("password2","").split("*")[2:]
    #     error = form.is_not_valid_person()

    #     #Нет ошибок
    #     if not error: 
    #         user = form.save(commit=True) #commit=True - не обязательно (default), но в напоминание!
    #         login(request, user)
    #         return redirect(reverse_lazy("profile"))
        
    #     #Есть ошибки
    #     if type(error) == tuple: #Такой пользователь уже существует
    #         context["error"] = error[0]
    #         redirect(login_view)

    #     context["error"] = error

    return render(request, TEML_ROOT+"register.html", context)

def login_view(request):
    context = {}
    if re.search(r"/myauth/login/\?next=/advertisement-post/", request.META["HTTP_REFERER"]): #"http://127.0.0.1:8000/myauth/login/?next=/advertisement-post/"
        context["error"] = "Для создания объявления сначала надо авторизоваться."

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None: # authenticate return "user", so he in our DB
            login(request, user)
            return redirect(profile)
        context["error"] = "Пользователь не найден." # authenticate return "none", so he not in our DB

    return render(request, TEML_ROOT+"login.html", context)

#@login_required(login_url = reverse_lazy("login")) # To login you have to login 
def profile(request):
    context = {"req" : request}
    return render(request, TEML_ROOT+"profile.html", context)

def exit(request):
    logout(request)
    return redirect(MAIN_PAGE_RESPONSE)