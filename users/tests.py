from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class RegistrationTestCase(TestCase):
    def test_user_account_created(self):
        self.client.post(reverse("users:register"), data={
            "username": "javoh",
            "first_name": "giyos",
            "last_name": "toshmatov",
            "email": "giyosoripov4@gmail.com",
            "password": "jsdlk",
        })

        user = User.objects.get(username="javoh")

        self.assertEqual(user.first_name, 'giyos')
        self.assertEqual(user.last_name, 'toshmatov')
        self.assertEqual(user.email, 'giyosoripov4@gmail.com')
        self.assertNotEqual(user.password, 'jsdlk')
        self.assertTrue(user.check_password("jsdlk"))

    def test_required_fields(self):
        response = self.client.post(reverse("users:register"), data={
            "first_name": "akbar",
            "email": "giyos@kcsdj.com",
        })

        user_count = User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "username", "This field is required.")
        self.assertFormError(response, "form", "password", "This field is required.")

    def test_invalid_email(self):
        response = self.client.post(reverse("users:register"), data={
            "username": "javoh",
            "first_name": "giyos",
            "last_name": "toshmatov",
            "email": "giyosoripov4",
            "password": "jsdlk",
        })

        user_count = User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "email", "Enter a valid email address.")

    def test_unique_username(self):
        user = User.objects.create(username="giyos", first_name="fhk", last_name="sifkd", email="scdjl@jvsd.com",
                                   password="231331")

        response = self.client.post(reverse("users:register"), data={
            "username": "giyos",
            "first_name": "giyos",
            "last_name": "toshmatov",
            "email": "giyosoripov4",
            "password": "jsdlk"
            , })

        user_count = User.objects.count()
        self.assertEqual(user_count,1)
        self.assertFormError(response,"form","username","A user with that username already exists.")


