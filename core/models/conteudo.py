from unittest.util import _MAX_LENGTH
from django.db import models

from core.models import Midia

class Conteudo(models.Model):
    topico = models.CharField(max_length=45)
    paragrafo = models.TextField(max_length=255)
    titulo = models.CharField(max_length=45)

    id_midia = models.ForeignKey(
        Midia, on_delete=models.PROTECT, related_name="conteudo"
    )

    def __str__(self):
        return self.topico