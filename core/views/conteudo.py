from rest_framework.viewsets import ModelViewSet

from core.models import Conteudo
from core.serializers import ConteudoSerializer


class ConteudoViewSet(ModelViewSet):
    queryset = Conteudo.objects.all()
    serializer_class = ConteudoSerializer