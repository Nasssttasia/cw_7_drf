from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    name = models.CharField(max_length=50, verbose_name='имя', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

