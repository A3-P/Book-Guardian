from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.contrib.auth import login
from django.views.generic.edit import FormView

class HomeList(ListView):
    model = models.BookGuardian
    template_name = "index.html"
    context_object_name = "bookguardian"


# User
class LoginRoute(LoginView):
    template_name = "login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("bookguardian:index")



class RegisterUser(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('bookguardian:index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('bookguardian:index')
        return super(RegisterUser, self).get(*args, **kwargs)

    def get_form(self, form_class=None):
        form = super(RegisterUser, self).get_form(form_class)

        form.fields['username'].widget.attrs['placeholder'] = "Digite o seu Email"
        form.fields['password1'].widget.attrs['placeholder'] = 'Digite a sua Senha'
        form.fields['password2'].widget.attrs['placeholder'] = 'Confirme a Senha'
        return form
