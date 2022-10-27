from rest_framework.viewsets import ModelViewSet

from core.models import Midia
from core.serializers import MidiaSerializer

class MidiaViewSet(ModelViewSet):
    queryset = Midia.objects.all()
    serializer_class = MidiaSerializer