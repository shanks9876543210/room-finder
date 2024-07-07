# models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username
