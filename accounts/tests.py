from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# test fonctionnel
class TestAuth(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(

            username="maman",

            password="fallene"

        )

    def test_login_valide(self):
        """Connexion avec identifiants corrects """
        response = self.client.post(

            reverse("login"),

            {

                "username": "maman",

                "password": "fallene"

            }

        )

        self.assertEqual(response.status_code, 302)


    def test_login_invalide(self):
        """Rejet avec mauvais mot de passe """
        response = self.client.post(

        reverse("login"),

        {
            "username": "maman",

            "password": "fallen"

        }

    )

        self.assertEqual(response.status_code, 200)



    def test_register(self):
        """Inscription d'un nouvel utilisateur"""
        response = self.client.post(

        reverse("register"),

        {

            "username": "fatou",

            "password1": "fatou1234",

            "password2": "fatou1234"

        }

    )

        self.assertEqual(response.status_code, 200)

    