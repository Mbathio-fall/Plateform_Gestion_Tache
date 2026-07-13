from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.


#vue register
def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            
            user = form.save()

            login(request, user)
            return redirect("login")

    else:

        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


#vue profil
@login_required
def profil(request):

    return render(request,"profil.html")