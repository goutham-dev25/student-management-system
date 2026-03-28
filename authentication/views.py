from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def login_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect("/login.html")

    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        messages.success(request, "Welcome back.")
        return redirect("/index.html")
    return render(request, "pages/login.html", {"form": form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect("/index.html")

    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Your account has been created.")
        return redirect("/index.html")
    return render(request, "pages/register.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("/login.html")
