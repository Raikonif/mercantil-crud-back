from django.db import models


class Task(models.Model):
    class Status(models.TextChoices):
        PENDING = "PEN", "Pending"
        IN_PROCESS = "PROCESS", "In process"
        FINISHED = "FIN", "Finished"

    class Priority(models.TextChoices):
        LOW = "LOW", "Low"
        MEDIUM = "MEDIUM", "Medium"
        HIGH = "HIGH", "High"

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    limit_date = models.DateField()

    class Meta:
        ordering = ["-created_at", "-id"]

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    task = models.ForeignKey(
        Task,
        related_name="comments",
        on_delete=models.CASCADE,
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "-id"]

    def __str__(self) -> str:
        return self.comment[:50]
