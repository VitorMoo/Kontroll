from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    telephone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    login_attempts = models.PositiveIntegerField(default=0)
    last_failed_login = models.DateTimeField(null=True, blank=True)
    lock_until = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ('User')
        verbose_name_plural = ('Users')

    def __str__(self):
        return self.username
