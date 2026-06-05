from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel
from authentication.models.role import Role


class CustomUser(AbstractUser, BaseModel):
    email = models.CharField(max_length=255, unique=True, blank=False, null=False)
    full_name = models.CharField(max_length=255, blank=False, null=False)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=False, blank=False, related_name="users")
    is_verified = models.BooleanField(default=False, null=True, blank=True)
    verification_token = models.CharField(max_length=255, blank=True, null=True)
    verification_token_expires_at = models.DateTimeField(blank=True, null=True)
    avatar_url = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=255, unique=True, blank=False, null=False)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]
        db_table = "auth_user"
        indexes = [models.Index(fields=["email"])]
