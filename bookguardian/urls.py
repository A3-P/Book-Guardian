from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomeList.as_view(), name="index"),
 ]

