from unittest.util import _MAX_LENGTH
from django.db import models


class Resposta(models.Model):
    textoresp = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.textoresp