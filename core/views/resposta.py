from rest_framework.viewsets import ModelViewSet

from core.models import Resposta
from core.serializers import RespostaSerializer

class RespostaViewSet(ModelViewSet):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer