from django.contrib import admin

from core.models import Conteudo, Formulario, Midia, Pergunta, Resposta

admin.site.register(Resposta)
admin.site.register(Pergunta)
admin.site.register(Formulario)
admin.site.register(Conteudo)
admin.site.register(Midia)

