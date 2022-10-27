from rest_framework.serializers import ModelSerializer

from core.models import Usuario


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'first_name', 'last_name', 'password', 'email', 'username')