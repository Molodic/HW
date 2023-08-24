from django.urls import path
from .views import register, login, profile, logout

urlpatterns = [
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("login/", login, name="login"),
    path("logout/", exit, name="logout")
]