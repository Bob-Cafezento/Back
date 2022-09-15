from django.db import models

class Resposta(models.Model):
    textpresp = models.CharField(max_length=100)

    def __str__(self):
            return self.textpresp

class Pergunta(models.Model):
    alternativas = models.CharField(max_length=100)
    texto_per = models.CharField(max_length=100)

    def __str__(self):
        return self.alternativas


class Formulario(models.Model):
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

class Sel_res_form(models.Model):
    odth = models.DateField()
    cod_form = models.IntegerField()

    def __str__(self):
        return self.odth


class Responde(models.Model):
    cod_form = models.IntegerField()
    dth = models.DateField()

    def __str__(self):
        return self.cod_form
