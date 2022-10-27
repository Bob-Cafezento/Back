from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    nome = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    senha = models.CharField(max_length=35, null=True, blank=True)