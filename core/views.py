from rest_framework.viewsets import ModelViewSet
from core.models import Resposta, Pergunta, Formulario, Conteudo, Midia

# from rest_framework.permissions import IsAuthenticated
# permission_classes = [IsAuthenticated]
# Acima temos as permissões DRF, caso seja necessário proteger o conteúdo no views

from core.serializers import (
    RespostaSerializer,
    PerguntaSerializer,
    FormularioSerializer,
    ConteudoSerializer,
    MidiaSerializer,
)


class RespostaViewSet(ModelViewSet):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer


class PerguntaViewSet(ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer


class FormularioViewSet(ModelViewSet):
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer


class ConteudoViewSet(ModelViewSet):
    queryset = Conteudo.objects.all()
    serializer_class = ConteudoSerializer


class MidiaViewSet(ModelViewSet):
    queryset = Midia.objects.all()
    serializer_class = MidiaSerializer
