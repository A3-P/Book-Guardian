from django.shortcuts import render
from django.views.generic.list import ListView
from . import models


class HomeList(ListView):
    model = models.BookGuardian
    template_name = "index.html"
    context_object_name = "bookguardian"
