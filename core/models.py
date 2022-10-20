from unittest.util import _MAX_LENGTH
from django.db import models




class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=35)

    def __str__(self):
        return self.nome

class Resposta(models.Model):
    cod_resp = models.IntegerField
    textoresp = models.CharField(max_length=250)
    cod_p = models.IntegerField()

    def __str__(self):
            return self.cod_resp


class Formulario(models.Model):
    cod_form = models.IntegerField()
    titulo = models.CharField(max_length=50)
    data_inicial = models.DateField()

    cod_p = models.ForeignKey(
        Pergunta, on_delete=models.PROTECT, related_name="formulario"
        )
    cod_user = models.ForeignKey(
        Usuario, on_delete=models.PROTECT, related_name="formulario"
    )

    def __str__(self):
        return self.cod_form

class Midia(models.Model):
    id_midia = models.IntegerField()
    link = models.URLField()
    videos = models.FileField()
    imagens = models.ImageField()
    audios = models.FileField()
    
    def __str__(self):
        return self.id_midia

class Conteudo(models.Model):
    id_conteudo = models.IntegerField()
    topico = models.CharField(max_length=45)
    paragrafo = models.TextField(max_length=255)
    titulo = models.CharField(max_length=45)
    
    id_midia = models.ForeignKey(
        Midia, on_delete=models.PROTECT, related_name="conteudo"
    )
    
    def __str__(self):
        return self.id_conteudo

class Pergunta(models.Model):
    cod_p = models.IntegerField()
    alternativas = models.CharField(max_length=100)
    texto_per = models.TextField(max_length=100)
    cod_form = models.IntegerField()

    id_conteudo = models.ForeignKey(
        
    )

    def __str__(self):
        return self.cod_p
    