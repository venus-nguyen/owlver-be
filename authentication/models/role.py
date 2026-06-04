from django.db import models
from core.models import BaseModel


class Role(BaseModel):

    ADMIN = "admin"
    USER = "user"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (USER, "User"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
