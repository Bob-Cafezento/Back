from rest_framework.viewsets import ModelViewSet

from core.models import Disciplina, Conteudo, Alternativa, Pergunta, Formulario
from core.serializers import (
    DisciplinaSerializer,
    ConteudoSerializer,
    AlternativaSerializer,
    PerguntaSerializer,
    FormularioSerializer,
    FormularioDetailSerializer,
)


class DisciplinaViewSet(ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class ConteudoViewSet(ModelViewSet):
    queryset = Conteudo.objects.all()
    serializer_class = ConteudoSerializer


class AlternativaViewSet(ModelViewSet):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer


class PerguntaViewSet(ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer


class FormularioViewSet(ModelViewSet):
    queryset = Formulario.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return FormularioDetailSerializer
        return FormularioSerializer
