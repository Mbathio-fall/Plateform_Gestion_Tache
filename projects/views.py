from pyexpat.errors import messages

from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import projects
from .models import Projet, Tache

#vue dashboard

@login_required

def dashboard(request):
    projets = Projet.objects.all()

    return render(request,"dashboard.html",{"projets": projets})


# vue projet_create

@login_required
def projet_create(request):

    if request.method == "POST":
          Projet.objects.create(
            nom=request.POST.get("nom"),
            description=request.POST.get("description"),
            createur=request.user
        )
          messages.success(request, "Le projet a été créé avec succès.")

          
          return redirect("dashboard")

    return render(request,"projet_create.html")


    
# vues projet_detail

@login_required
def projet_detail(request, id): 
  projet = get_object_or_404(Projet, id=id)
  taches = Tache.objects.filter(projet=projet)

  return render(request,"projet_detail.html",{"projet": projet , "taches": taches,
})



# vues projet_delete

@login_required
def projet_delete(request, id):
    projet = get_object_or_404(Projet, id=id)

    if projet.createur != request.user:
        return HttpResponseForbidden(
            "Vous n'avez pas l'autorisation de supprimer ce projet."
        )

    projet.delete()
    messages.success(request, "Le projet a été supprimé avec succès.")
    return redirect("dashboard")

# vues projet_update

@login_required
def projet_update(request, id):

    projet = get_object_or_404(Projet, id=id)

    if request.method == "POST":
     projet.nom = request.POST.get("nom")
     projet.description = request.POST.get("description")
     projet.save()
     return redirect("dashboard")

    return render(request,"projet_update.html", {"projet": projet}
    )



# vues tache_create

from django.contrib.auth.models import User

@login_required
def tache_create(request):

    if request.method == "POST":

        Tache.objects.create(
            titre=request.POST.get("titre"),
            description=request.POST.get("description"),
            projet=Projet.objects.get(id=request.POST.get("projet")),
            assigne=User.objects.get(id=request.POST.get("assigne")),
            statut=request.POST.get("statut"),
            priorite=request.POST.get("priorite"),
            deadline=request.POST.get("deadline"),
        )
        messages.success(request, "La tâche a été créée avec succès.")

        return redirect("dashboard")

    projets = Projet.objects.all()
    utilisateurs = User.objects.all()

    return render(request, "tache_create.html", {
        "projets": projets,
        "utilisateurs": utilisateurs,
    })

        

# vues tache_detail

@login_required
def tache_detail(request, id):

    tache = get_object_or_404(Tache, id=id)

    return render( request, "tache_detail.html",{"tache": tache})


# vues tache_dlete

@login_required
def tache_delete(request, id):

    tache = get_object_or_404(Tache, id=id)

    tache.delete()

    return redirect("dashboard")



# vues tache_update

@login_required
def tache_update(request, id):
    tache = get_object_or_404(Tache, id=id)

    if request.method == "POST":
        tache = Tache.objects.get(id=id)
        tache.titre = request.POST.get("titre")
        tache.description = request.POST.get("description")
        tache.save()
        return redirect("dashboard")
    return render(request,"tache_update.html",{"tache": tache}
)
