from django.urls import path
from .views import register, login_view, profile, exit

urlpatterns = [
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("login/", login_view, name="login"),
    path("logout", exit, name="logout")
]