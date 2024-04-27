from django.urls import path

from . import views

app_name = "bookguardian"

urlpatterns = [
    # BookGuardian
    path("", views.HomeList.as_view(), name="index"),
    # User
    path("login/", views.LoginRoute.as_view(), name="login"),
]
