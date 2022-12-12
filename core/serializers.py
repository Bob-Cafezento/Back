from django.contrib.auth.models import Group

from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,
    HiddenField,
    ModelSerializer,
)

from core.models import Alternativa, Conteudo, Formulario, Pergunta


class CustomRegisterSerializer(RegisterSerializer):
    def save(self, request):
        user = super().save(request)
        user.groups.add(Group.objects.get(name="estudante"))
        user.save()
        return user


class UserDetailNestedSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = ["pk", "username", "first_name", "last_name"]
        depth = 1


class ConteudoSerializer(ModelSerializer):
    criado_por = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Conteudo
        fields = "__all__"


class AlternativaSerializer(ModelSerializer):
    class Meta:
        model = Alternativa
        fields = "__all__"


class PerguntaSerializer(ModelSerializer):
    alternativas = AlternativaSerializer(many=True)

    class Meta:
        model = Pergunta
        fields = "__all__"
        depth = 1


class PerguntaDetailSerializer(ModelSerializer):
    alternativas = AlternativaSerializer(many=True, read_only=True)

    class Meta:
        model = Pergunta
        fields = "__all__"
        depth = 1


class FormularioSerializer(ModelSerializer):
    conteudo = CharField(source="conteudo.nome")
    criado_por = HiddenField(default=CurrentUserDefault())
    perguntas = PerguntaSerializer(many=True)

    class Meta:
        model = Formulario
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        perguntas = validated_data.pop("perguntas")
        conteudo = validated_data.pop("conteudo")
        perguntasFormulario = []
        alternativas = []

        for pergunta in perguntas:

            for alternativa in pergunta["alternativas"]:
                alternativaCriada = Alternativa.objects.create(**alternativa)
                alternativaCriada.save()
                alternativas.append(alternativaCriada.id)

            perguntaCriada = Pergunta.objects.create(
                texto_pergunta=pergunta["texto_pergunta"]
            )
            perguntaCriada.save()
            perguntaCriada.alternativas.set(alternativas)

            perguntasFormulario.append(perguntaCriada.id)
            alternativas.clear()

        conteudo_id = Conteudo.objects.values().get(nome=conteudo["nome"])["id"]

        formulario = Formulario.objects.create(
            conteudo_id=conteudo_id, **validated_data
        )
        formulario.save()
        formulario.perguntas.set(perguntasFormulario)
        return formulario

    def update(self, instance, validated_data):
        if validated_data.get("titulo") != None:
            titulo = validated_data.pop("titulo")
        else:
            titulo = None
        if validated_data.get("perguntas") != None:
            perguntas = validated_data.pop("perguntas")
        else:
            perguntas = None
        perguntasFormulario = []
        alternativas = []

        if perguntas != None or titulo != None:
            if titulo != None:
                instance.titulo = ""
            else:
                titulo = instance.titulo
            if perguntas != None:
                instance.perguntas.all().delete()

                for pergunta in perguntas:
                    for alternativa in pergunta["alternativas"]:
                        alternativaCriada = Alternativa.objects.create(**alternativa)
                        alternativaCriada.save()
                        alternativas.append(alternativaCriada.id)

                    perguntaCriada = Pergunta.objects.create(
                        texto_pergunta=pergunta["texto_pergunta"]
                    )
                    perguntaCriada.save()
                    perguntaCriada.alternativas.set(alternativas)

                    perguntasFormulario.append(perguntaCriada.id)
                    alternativas.clear()

            else:
                for pergunta in instance.perguntas.all():
                    print(pergunta)
                    perguntasFormulario.append(pergunta.id)

            conteudo_id = Conteudo.objects.values().get(nome=instance.conteudo.nome)[
                "id"
            ]

            instance.conteudo_id = conteudo_id
            instance.titulo = titulo
            instance.save()
            instance.perguntas.set(perguntasFormulario)
        return instance


class FormularioDetailSerializer(ModelSerializer):
    perguntas = PerguntaDetailSerializer(many=True, read_only=True)
    conteudo = CharField(source="conteudo.nome")
    criado_por = UserDetailNestedSerializer()

    class Meta:
        model = Formulario
        fields = "__all__"
        depth = 1
