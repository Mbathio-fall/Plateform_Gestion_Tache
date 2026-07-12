from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Projet, Tache

# Create your tests here.
# test unitaire
class TestModeleProjet(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(

            username="Mariama",

            password="yama5555"

        )
    def test_creation_projet(self):
        """Un projet doit etre créer correctement"""
        projet = Projet.objects.create(
            nom="Mise en place d'un reseau securisé",
            description="securisé le reseau avec firewall",
            createur=self.user
        )

        self.assertEqual(projet.nom, "Mise en place d'un reseau securisé")
        self.assertEqual(projet.createur.username, "Mariama")

    def test_str_projet(self):
        projet = Projet.objects.create(
            nom="developpement site e-commerce",
            description="Telelecharger django",
            createur=self.user
        )
        
        self.assertEqual(str(projet), "developpement site e-commerce")


class TestModeleTache(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="sophia",
            password="phia5555"
        )
        self.Projet = Projet.objects.create(
            nom="site vitrine",
            description="creation des different pages",
            createur=self.user
        )

    def test_statut_defaut(self):
        """la page doit affiche le status todo par defaut"""
        tache = Tache.objects.create(
            titre="planification du projet",
            description="definir les cahier des charges",
            projet=self.Projet,
            assigne=self.user
        )

        self.assertEqual(tache.statut, "todo")


    def test_relation_projet(self) :
        """La tâche doit etre liée au bon projet"""
        tache = Tache.objects.create(
            titre="planification du projet",
            description="definir les cahier des charges",
            projet=self.Projet,
            assigne=self.user
        )
        self.assertEqual(tache.projet, self.Projet)



class TestVueDashboard(TestCase):

    def setUp(self):

        self.client = Client()

        self.user = User.objects.create_user(
            username="mbaye",
            password="123456789"
        
        )

    def test_dashboard_200(self):
        """la page dashboard doit retourner 200"""
        self.client.login(
            username="mbaye",
            password="123456789"
        )

        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)

def test_redirect_non_auth(self):
        """Redirection vers login si l'utilisateur n'est pas  connecté"""

        response = self.client.get(
            reverse("dashboard")
        )

        self.assertEqual(response.status_code, 302)




