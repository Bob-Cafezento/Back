from rest_framework.viewsets import ModelViewSet

from core.models import Alternativa, Conteudo, Formulario, Pergunta
from core.serializers import (
    AlternativaSerializer,
    ConteudoSerializer,
    FormularioDetailSerializer,
    FormularioSerializer,
    PerguntaDetailSerializer,
    PerguntaSerializer,
)


class ConteudoViewSet(ModelViewSet):
    queryset = Conteudo.objects.all()
    serializer_class = ConteudoSerializer

    def get_queryset(self):
        disciplina = self.request.query_params.get("disciplina")

        return Conteudo.objects.filter(disciplina=disciplina)


class AlternativaViewSet(ModelViewSet):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer


class PerguntaViewSet(ModelViewSet):
    queryset = Pergunta.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PerguntaDetailSerializer
        return PerguntaSerializer


class FormularioViewSet(ModelViewSet):
    queryset = Formulario.objects.all()

    def get_queryset(self):
        id_conteudo = self.request.query_params.get("conteudo")

        if id_conteudo != None:
            return Formulario.objects.filter(conteudo=id_conteudo)
        return Formulario.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return FormularioDetailSerializer
        return FormularioSerializer
