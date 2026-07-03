from django.shortcuts import render
from .models import Projet

# Create your views here.


def dashboard(request):
    projets = Projet.objects.all()

    return render(
        request,
        "dashboard.html",
        {"projets": projets}
    )