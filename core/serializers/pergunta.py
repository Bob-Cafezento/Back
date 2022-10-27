from rest_framework.serializers import ModelSerializer

from core.models import Pergunta

class PerguntaSerializer(ModelSerializer):
    class Meta:
        model = Pergunta
        fields = "__all__"