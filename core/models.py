from unittest.util import _MAX_LENGTH
from django.db import models


# class Usuario(models.Model):
#     nome = models.CharField(max_length=30)
#     email = models.CharField(max_length=50)
#     senha = models.CharField(max_length=35)

#     def __str__(self):
#         return self.nome


class Midia(models.Model):
    link = models.URLField(blank=True)
    videos = models.FileField(blank=True)
    imagens = models.ImageField(blank=True)
    audios = models.FileField(blank=True)


class Conteudo(models.Model):
    topico = models.CharField(max_length=45)
    paragrafo = models.TextField(max_length=255)
    titulo = models.CharField(max_length=45)

    id_midia = models.ForeignKey(
        Midia, on_delete=models.PROTECT, related_name="conteudo"
    )

    def __str__(self):
        return self.id_conteudo


class Resposta(models.Model):
    textoresp = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.cod_resp


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


class Formulario(models.Model):
    titulo = models.CharField(max_length=50)
    data_inicial = models.DateField(null=True, blank=True)

    pergunta = models.ForeignKey(
        Pergunta, on_delete=models.PROTECT, related_name="formularios", default=""
    )
    # usuario = models.ForeignKey(
    #     Usuario, on_delete=models.PROTECT, related_name="formulario"
    # )

    def __str__(self):
        return self.titulo
