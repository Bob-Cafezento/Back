from rest_framework.viewsets import ModelViewSet

from core.models import Pergunta
from core.serializers import PerguntaSerializer


class PerguntaViewSet(ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer