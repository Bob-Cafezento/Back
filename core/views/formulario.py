from rest_framework.viewsets import ModelViewSet

from core.models import Formulario
from core.serializers import FormularioSerializer

class FormularioViewSet(ModelViewSet):
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer