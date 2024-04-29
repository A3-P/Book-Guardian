from django.urls import path

from . import views

app_name = "bookguardian"

urlpatterns = [
    # BookGuardian
    path("", views.HomeList.as_view(), name="index"),
    path("setting/", views.configPage.as_view(), name="config"),
    # User
    path("login/", views.LoginRoute.as_view(), name="login"),
    path("register/", views.RegisterUser.as_view(), name="register-user"),
    path("logout/", views.custom_logout, name="logout"),
]
