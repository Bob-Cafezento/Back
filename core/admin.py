from django.contrib import admin

from core.models import Resposta, Pergunta, Formulario, Sel_res_form, Responde

admin.site.register(Resposta)
admin.site.register(Pergunta)
admin.site.register(Formulario)
admin.site.register(Sel_res_form)
admin.site.register(Responde)