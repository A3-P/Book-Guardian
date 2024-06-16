from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from userauths.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Nome de Usuário"}),
        error_messages={"unique": "Este nome de usuário já está em uso."},
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email"}),
        error_messages={"unique": "Este email já está em uso."},
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Senha"}),
        error_messages={"required": "Este campo é obrigatório."},
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirme a Senha"}),
        error_messages={"required": "Este campo é obrigatório."},
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data["username"].lower()
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nome de usuário já está em uso.")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este email já está em uso.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("As senhas não coincidem.")

        if len(password1) < 8:
            raise ValidationError("A senha deve conter no mínimo 8 caracteres.")

        if self.cleaned_data["username"] in password1:
            raise ValidationError("A senha é muito semelhante ao nome de usuário.")

        return password2


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Digite o seu email"}),
        error_messages={
            "required": "Este campo é obrigatório.",
            "invalid": ("Informe um endereço de email válido."),
        },
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Senha"}),
        error_messages={"required": "Este campo é obrigatório."},
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError(("Email ou senha incorretos."))
        return cleaned_data
