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
    class Meta:
        model = Pergunta
        fields = "__all__"


class PerguntaDetailSerializer(ModelSerializer):
    alternativas = AlternativaSerializer(many=True, read_only=True)

    class Meta:
        model = Pergunta
        fields = "__all__"
        depth = 1


class FormularioSerializer(ModelSerializer):
    conteudo = CharField(source="conteudo.nome")
    criado_por = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Formulario
        fields = "__all__"


class FormularioDetailSerializer(ModelSerializer):
    perguntas = PerguntaDetailSerializer(many=True, read_only=True)
    conteudo = CharField(source="conteudo.nome")
    criado_por = UserDetailNestedSerializer()

    class Meta:
        model = Formulario
        fields = "__all__"
        depth = 1
