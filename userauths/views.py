from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from userauths.forms import UserRegisterForm
from userauths.models import User


def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, f"You are already logged in.")
        return redirect("bookguardian:index")

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            new_user = form.save()  # new_user.email
            username = form.cleaned_data.get("username")
            # username = request.POST.get("username")
            messages.success(
                request, f"Hey {username}, your account was created successfully."
            )
            # new_user = authenticate(username=form.cleaned_data.get('email'))
            new_user = authenticate(
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
            )
            login(request, new_user)
            return redirect("bookguardian:index")

    else:
        form = UserRegisterForm()
    context = {"form": form}
    return render(request, "userauths/sign-up.html", context)


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            new_user = form.save()

            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Hello {username} your account was created success."
            )

            new_user = authenticate(
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
            )

            login(request, new_user)

            return redirect("bookguardian:index")

    if request.user.is_authenticated:
        messages.warning(request, f"You are logged in")
        return redirect("bookguardian:index")

    else:
        form = UserRegisterForm()
    context = {"form": form}
    return render(request, "sign-up.html", context)


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:  # if there is a user
                login(request, user)
                messages.success(request, "You are logged.")
                return redirect("bookguardian:index")
            else:
                messages.warning(request, "Username or password does not exist")
                return redirect("userauths:sign-in")
        except:
            messages.warning(request, "User does not exist")

    if request.user.is_authenticated:
        messages.warning(request, "You are already logged In")
        return redirect("bookguardian:index")

    return render(request, "sign-in.html")


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("bookguardian:ladinpage")
