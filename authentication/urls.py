from django.urls import path

from .views import login_view, logout_view, register_view

urlpatterns = [
    path("login.html", login_view, name="login"),
    path("register.html", register_view, name="register"),
    path("logout.html", logout_view, name="logout"),
]
