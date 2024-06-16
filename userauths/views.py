from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from userauths.forms import UserRegisterForm
from userauths.models import User

from .forms import UserLoginForm


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Olá {username}, sua conta foi criada com sucesso."
            )
            new_user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
            )
            login(request, new_user)
            return redirect("bookguardian:index")
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = UserRegisterForm()

    if request.user.is_authenticated:
        messages.warning(request, "Você já está logado.")
        return redirect("bookguardian:index")

    context = {"form": form}
    return render(request, "sign-up.html", context)


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Você está logado")
                return redirect("bookguardian:index")
        else:
            messages.warning(request, "Por favor, corrija os erros abaixo.")
    else:
        form = UserLoginForm()

    if request.user.is_authenticated:
        messages.warning(request, "Você já está logado.")
        return redirect("bookguardian:index")

    return render(request, "sign-in.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("bookguardian:ladinpage")
