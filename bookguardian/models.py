from django.contrib.auth.models import User
from django.db import models


class BookGuardian(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    profile_image = models.ImageField(
        upload_to="profileImage/%Y/%m/", blank=True, null=True
    )
    book_image = models.ImageField(
        upload_to="bookImage/%Y/%m/", blank=False, null=False
    )
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    author_book = models.CharField(
        max_length=100, blank=True, null=True, default="desconhecido"
    )
    category = models.CharField(
        default="generico",
        max_length=50,
        # Status
        choices=(
            ("F", "Ficcao"),
            ("R", "Romance"),
            ("T", "Terro"),
            ("FA", "Fantasia"),
            ("NF", "Nao ficcao"),
            ("MHQ", "Manga e HQ"),
        ),
        blank=True,
        null=True,
    )
    read = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
