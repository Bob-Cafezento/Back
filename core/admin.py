from django.contrib import admin

from core.models import Alternativa, Conteudo, Formulario, Pergunta

admin.site.register(Conteudo)
admin.site.register(Alternativa)
admin.site.register(Pergunta)
admin.site.register(Formulario)
