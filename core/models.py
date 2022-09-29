from django.db import models

class Resposta(models.Model):
    cod_resp = models.IntegerField()
    status = models.CharField(max_length=100)
    textpresp = models.CharField(max_length=250)

    def __str__(self):
            return self.cod_resp

class Pergunta(models.Model):
    cod_p = models.IntegerField()
    gabarito = models.CharField(max_length=5)
    alternativas = models.CharField(max_length=250)
    texto_per = models.TextField(max_length=500)

    def __str__(self):
        return self.cod_p


class Formulario(models.Model):
    cod_form = models.IntegerField()
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return self.cod_form

class Sel_res_form(models.Model):
    cod_form = models.IntegerField()
    odth = models.DateField()

    def __str__(self):
        return self.cod_form

class Responde(models.Model):
    cod_form = models.IntegerField()
    dth = models.DateField()

    def __str__(self):
        return self.cod_form
    
class Conteudo(models.Model):
    id_conteudo = models.IntegerField()
    titulo = models.CharField(max_length=200)
    paragrafo = models.TextField(max_length=2000)
    topico = models.CharField(max_length=150)
    
    def __str__(self):
        return self.id_conteudo

class Midia(models.Model):
    cod_midia = models.IntegerField()
    imagens = models.ImageField()
    audios = models.FileField()
    videos = models.FileField()
    
    def __str__(self):
        return self.cod_midia
    