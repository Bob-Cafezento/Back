from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import Group
from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

from core.models import Disciplina, Conteudo, Alternativa, Pergunta, Formulario


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


class DisciplinaSerializer(ModelSerializer):
    class Meta:
        model = Disciplina
        fields = "__all__"


class ConteudoSerializer(ModelSerializer):
    class Meta:
        model = Conteudo
        fields = "__all__"


class AlternativaSerializer(ModelSerializer):
    class Meta:
        model = Alternativa
        fields = "__all__"


class PerguntaSerializer(ModelSerializer):
    alternativas = AlternativaSerializer(many=True, read_only=True)

    class Meta:
        model = Pergunta
        fields = "__all__"


class FormularioSerializer(ModelSerializer):
    class Meta:
        model = Formulario
        fields = "__all__"


class FormularioDetailSerializer(ModelSerializer):
    perguntas = PerguntaSerializer(many=True, read_only=True)
    criado_por = UserDetailNestedSerializer()

    class Meta:
        model = Formulario
        fields = "__all__"
        depth = 1
