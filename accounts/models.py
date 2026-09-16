from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin / Manager"
        INVENTORY = "INVENTORY", "Inventory staff"
        SALES = "SALES", "Sales staff"
        VIEWER = "VIEWER", "Viewer"

    role = models.CharField(max_length=20,choices=Role.choices, default=Role.VIEWER)
    phone = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"