from django.urls import path

from . import views

app_name = "bookguardian"

urlpatterns = [
    # BookGuardian
    path("", views.LadinPage.as_view(), name="ladinpage"),
    path("index/", views.HomeList.as_view(), name="index"),
    path("settings/", views.PageConfig.as_view(), name="settings"),
    path("book/", views.PageBook.as_view(), name="book"),
    path("newbook/", views.PageNewBook.as_view(), name="newbook"),


    # User
    path("login/", views.LoginRoute.as_view(), name="login"),
    path("register/", views.RegisterUser.as_view(), name="register-user"),
    path("logout/", views.custom_logout, name="logout"),
]
