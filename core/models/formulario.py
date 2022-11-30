from unittest.util import _MAX_LENGTH

from django.db import models

from .pergunta import Pergunta


class Formulario(models.Model):
    titulo = models.CharField(max_length=50)
    data_inicial = models.DateField(null=True, blank=True)

    pergunta = models.ForeignKey(
        Pergunta, on_delete=models.PROTECT, related_name="formularios",
    )

    def __str__(self):
        return self.titulo