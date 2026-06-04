from django.db import models
from core.models import BaseModel


class Role(BaseModel):

    ADMIN = "admin"
    STREAMER = "streamer"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (STREAMER, "Streamer"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='streamer')


