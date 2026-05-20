import uuid

from django.core.management.base import BaseCommand

from api.models import UserTest


USER_TEST_SEEDS = [
    ("1f1c7c6f-7365-4dc3-99e8-9ed62bff1cf7", "Alice"),
    ("b6d84ad9-f455-42e7-9cfc-87a1737ac73d", "Bob"),
    ("b3612179-8019-45e4-aa47-347a5de57670", "Carol"),
]


class Command(BaseCommand):
    help = "Create seed UserTest records."

    def handle(self, *args, **options):
        created_count = 0
        updated_count = 0

        for user_id, name in USER_TEST_SEEDS:
            _, created = UserTest.objects.update_or_create(
                id=uuid.UUID(user_id),
                defaults={"name": name},
            )

            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {len(USER_TEST_SEEDS)} user tests "
                f"({created_count} created, {updated_count} updated)."
            )
        )
