from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Disciplina(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Conteudo(models.Model):
    nome = models.CharField(max_length=150)
    disciplina = models.ForeignKey(
        Disciplina, on_delete=models.PROTECT, related_name="conteudos"
    )

    def __str__(self):
        return self.nome


class Alternativa(models.Model):
    texto_alternativas = models.CharField(max_length=150)
    esta_correta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto_alternativas


class Pergunta(models.Model):
    texto_pergunta = models.CharField(max_length=150)
    alternativas = models.ManyToManyField(Alternativa, related_name="+")

    def __str__(self):
        return self.texto_pergunta


class Formulario(models.Model):
    titulo = models.CharField(
        max_length=255, default=_("New Form"), verbose_name=_("Form Title")
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="formularios"
    )
    conteudo = models.ForeignKey(Conteudo, on_delete=models.DO_NOTHING)
    perguntas = models.ManyToManyField(Pergunta, related_name="+")

    def __str__(self):
        return self.titulo
