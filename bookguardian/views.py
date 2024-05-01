from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from . import models


class LadinPage(ListView):
    model = models.BookGuardian
    template_name = "ladinpage.html"
    context_object_name = "bookguardian"

class PageNewBook(LoginRequiredMixin, CreateView):
    model = models.BookGuardian
    fields = ['book_image', 'title', 'description', 'category', 'author_book',  'read']
    success_url = reverse_lazy('bookguardian:index')  #
    template_name = 'addBook.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PageNewBook, self).form_valid(form)

class PageDetailBook(LoginRequiredMixin, DetailView):
    model = models.BookGuardian
    context_object_name = 'bookguardian'
    template_name = 'bookPage.html'


class PageUpdateBook(LoginRequiredMixin, UpdateView):
    model = models.BookGuardian
    context_object_name = 'bookguardian'
    fields = ['book_image', 'title', 'description', 'category', 'author_book',  'read']
    success_url = reverse_lazy('bookguardian:index')  #
    template_name = 'updateBook.html'

class PageDeleteBook(LoginRequiredMixin, DeleteView):
    model = models.BookGuardian
    context_object_name = 'bookguardian'
    success_url =  reverse_lazy("bookguardian:index")
    template_name = 'bookguardian_confirm_delete.html'
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

class PageConfig(ListView):
    model = models.BookGuardian
    template_name = "configPage.html"
    context_object_name = "bookguardian"


class HomeList(LoginRequiredMixin, ListView):
    model = models.BookGuardian
    template_name = "index.html"
    context_object_name = "bookguardian"
    login_url = '/login/'  # Define a URL para redirecionar se o usuário não estiver logado

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = models.BookGuardian.objects.filter(user=user)
        else:
            # Redireciona o usuário para outra página se não estiver autenticado
            return reverse_lazy("bookguardian:ladinpage")
        return queryset


# User
class LoginRoute(LoginView):
    template_name = "login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("bookguardian:index")


class RegisterUser(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("bookguardian:index")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("bookguardian:index")
        return super(RegisterUser, self).get(*args, **kwargs)

    def get_form(self, form_class=None):
        form = super(RegisterUser, self).get_form(form_class)

        form.fields["username"].widget.attrs["placeholder"] = "Digite o seu User"
        form.fields["password1"].widget.attrs["placeholder"] = "Digite a sua Senha"
        form.fields["password2"].widget.attrs["placeholder"] = "Confirme a Senha"
        return form


def custom_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("bookguardian:ladinpage"))
