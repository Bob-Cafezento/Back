from rest_framework.serializers import ModelSerializer

from core.models import Resposta


class RespostaSerializer(ModelSerializer):
    class Meta:
        model = Resposta
        fields = "__all__"