from rest_framework.serializers import ModelSerializer

from core.models import Midia


class MidiaSerializer(ModelSerializer):
    class Meta:
        model = Midia
        fields = "__all__"