from rest_framework.serializers import ModelSerializer

from core.models import Conteudo

class ConteudoSerializer(ModelSerializer):
    class Meta:
        model = Conteudo
        fields = "__all__"