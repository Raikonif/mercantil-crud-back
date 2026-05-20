from io import StringIO

from django.core.management import call_command
from rest_framework import status
from rest_framework.test import APITestCase

from .models import UserTest


class UserTestViewSetTests(APITestCase):
    def test_create_user_test(self):
        response = self.client.post("/api/user-tests/", {"name": "Alice"}, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Alice")
        self.assertTrue(UserTest.objects.filter(name="Alice").exists())

    def test_list_user_tests(self):
        user_test = UserTest.objects.create(name="Bob")

        response = self.client.get("/api/user-tests/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(
            {"id": str(user_test.id), "name": "Bob"},
            response.data,
        )

    def test_retrieve_user_test(self):
        user_test = UserTest.objects.create(name="Carol")

        response = self.client.get(f"/api/user-tests/{user_test.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Carol")

    def test_update_user_test(self):
        user_test = UserTest.objects.create(name="Dave")

        response = self.client.patch(
            f"/api/user-tests/{user_test.id}/",
            {"name": "David"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user_test.refresh_from_db()
        self.assertEqual(user_test.name, "David")

    def test_delete_user_test(self):
        user_test = UserTest.objects.create(name="Eve")

        response = self.client.delete(f"/api/user-tests/{user_test.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(UserTest.objects.filter(id=user_test.id).exists())


class SeedUserTestsCommandTests(APITestCase):
    def test_seed_user_tests_command_creates_three_records(self):
        output = StringIO()

        call_command("seed_user_tests", stdout=output)

        self.assertEqual(UserTest.objects.count(), 3)
        self.assertEqual(
            list(UserTest.objects.order_by("name").values_list("name", flat=True)),
            ["Alice", "Bob", "Carol"],
        )
        self.assertIn("Seeded 3 user tests", output.getvalue())

    def test_seed_user_tests_command_is_idempotent(self):
        call_command("seed_user_tests", stdout=StringIO())
        call_command("seed_user_tests", stdout=StringIO())

        self.assertEqual(UserTest.objects.count(), 3)
