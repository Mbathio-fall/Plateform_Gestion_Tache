from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#creation model projet

class Projet(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    createur = models.ForeignKey(User, related_name="projets_crees", on_delete=models.CASCADE)
    membres = models.ManyToManyField(User, related_name="projets_membres")
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
      return self.nom                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    


# creation model tache 

STATUT_CHOICES = [
    ("todo", "À faire"),
    ("en_cours", "En cours"),
    ("termine", "Terminée"),
]

PRIORITE_CHOICES = [
    ("basse", "Basse"),
    ("moyenne", "Moyenne"),
    ("haute", "Haute"),
]


class Tache(models.Model):
   titre = models.CharField(max_length=200)
   description = models.TextField(blank=True)
   projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
   assigne = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
   statut = models.CharField(max_length=20,choices=STATUT_CHOICES,default="todo")
   priorite = models.CharField(max_length=20,choices=PRIORITE_CHOICES,default="basse")
   deadline = models.DateField(null=True,blank=True)
   date_creation = models.DateTimeField(auto_now_add=True)

   def __str__(self):
    return self.titre
   