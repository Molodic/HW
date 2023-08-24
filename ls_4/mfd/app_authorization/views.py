from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm

# For main-page response
from app_lesson_4.views import index

MAIN_PAGE_RESPONSE = index

TEML_ROOT = "app_authorization/"

# Create your views here.


# def advertisement_post(request):
#     return render(request, "app_lesson_4"+"register.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
    return render(request, TEML_ROOT+"register.html")

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated: # Already logged in? 
            return redirect(profile) 
        else: # Not login yet, so let him see page
            return render(request, TEML_ROOT+"login.html")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None: # authenticate return "user", so he in our DB
            login(request, user)
            return redirect(profile)
        return render(request, TEML_ROOT+"login.html", {"error": "Пользователь не найден."}) # authenticate return "none", so he not in our DB

#@login.required(login_url = reverse_lazy("login"))
def profile(request):
    context = {"req" : request}
    return render(request, TEML_ROOT+"profile.html", context)

def exit(request):
    logout(request.user)
    return redirect(MAIN_PAGE_RESPONSE)