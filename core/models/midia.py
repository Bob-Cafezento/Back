from unittest.util import _MAX_LENGTH
from django.db import models

class Midia(models.Model):
    link = models.URLField(blank=True)
    videos = models.FileField(blank=True)
    imagens = models.ImageField(blank=True)
    audios = models.FileField(blank=True)

    def __str__(self):
        return self.link