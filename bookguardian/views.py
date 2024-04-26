from django.shortcuts import render
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from . import models


class HomeList(ListView):
    model = models.BookGuardian
    template_name = "index.html"
    context_object_name = "bookguardian"

#User
class LoginRoute(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('bookguardian:index')
