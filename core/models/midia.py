from django.db import models


class Midia(models.Model):
    link = models.URLField(null=True, blank=True)
    videos = models.FileField(null=True, blank=True)
    imagens = models.ImageField(null=True, blank=True)
    audios = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.link