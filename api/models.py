import uuid
from typing import override

from django.db import models


class UserTest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    desc = models.BooleanField(default=False)

    @override
    def __str__(self) -> str:
        return str(self.name)
