from django.db import models

from .conteudo import Conteudo
from .resposta import Resposta


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