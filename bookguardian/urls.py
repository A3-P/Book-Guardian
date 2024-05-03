from django.urls import path

from . import views
from django.conf.urls import handler404

app_name = "bookguardian"

handler404 = views.Custom404View.as_view()

urlpatterns = [
    # BookGuardian
    path("", views.LadinPage.as_view(), name="ladinpage"),
    path("index/", views.HomeList.as_view(), name="index"),
    path("settings/", views.PageConfig.as_view(), name="settings"),
    path("newbook/", views.PageNewBook.as_view(), name="newbook"),
    path('book/<int:pk>/', views.PageDetailBook.as_view(), name='bookdetail'),
    path('book-update/<int:pk>/', views.PageUpdateBook.as_view(), name='bookupdate'),
    path('book-delete/<int:pk>/', views.PageDeleteBook.as_view(), name='bookdelete'),


    # User
    path("login/", views.LoginRoute.as_view(), name="login"),
    path("register/", views.RegisterUser.as_view(), name="register-user"),
    path("logout/", views.custom_logout, name="logout"),
]
