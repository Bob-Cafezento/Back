from unittest.util import _MAX_LENGTH
from django.db import models

from core.models import Conteudo, Resposta

class Pergunta(models.Model):
    alternativas = models.CharField(max_length=100)
    texto_per = models.TextField(max_length=100, null=True, blank=True)

    conteudo = models.ForeignKey(
        Conteudo, on_delete=models.PROTECT, related_name="perguntas", null=True, blank=True
    )
    resposta = models.ForeignKey(
        Resposta, on_delete=models.PROTECT, related_name="perguntas", null=True, blank=True
    )

    def __str__(self):
        return self.texto_per