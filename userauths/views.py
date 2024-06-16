from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from userauths.forms import UserRegisterForm
from userauths.models import User
from django.views import View
from .forms import UserLoginForm

class RegisterView(View):
    template_name = 'sign-up.html'
    form_class = UserRegisterForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "Você já está logado.")
            return redirect("bookguardian:index")
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "Você já está logado.")
            return redirect("bookguardian:index")

        form = self.form_class(request.POST)
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

        context = {'form': form}
        return render(request, self.template_name, context)

class LoginView(View):
    template_name = 'sign-in.html'
    form_class = UserLoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "Você já está logado.")
            return redirect("bookguardian:index")
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "Você já está logado.")
            return redirect("bookguardian:index")

        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Você está logado")
                return redirect("bookguardian:index")
            else:
                messages.warning(request, "Credenciais inválidas.")
        else:
            messages.warning(request, "Por favor, corrija os erros abaixo.")

        return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("bookguardian:ladinpage")
