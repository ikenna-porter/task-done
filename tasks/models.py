from django.db import models
from projects.models import Project
from django.conf import settings


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    recurring = models.BooleanField(default=False, null=True, blank=True)
    frequency = models.DurationField(
        null=True,
        blank=True,
        choices=[
            (3600, "hourly"),
            (86400, "daily"),
            (604800, "weekly"),
            (18144000, "monthly"),
            (217728000, "yearly"),
        ],
    )
    project = models.ForeignKey(
        Project, related_name="tasks", on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name="tasks",
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name
