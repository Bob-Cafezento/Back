from rest_framework.serializers import ModelSerializer


from core.models import Resposta, Pergunta, Formulario, Conteudo, Midia

class RespostaSerializer(ModelSerializer):
    class Meta:
        model = Resposta
        fields = "__all__"

class PerguntaSerializer(ModelSerializer):
    class Meta:
        model = Pergunta
        fields = "__all__"

class FormularioSerializer(ModelSerializer):
    class Meta:
        model = Formulario
        fields = "__all__"

class ConteudoSerializer(ModelSerializer):
    class Meta:
        model = Conteudo
        fields = "__all__"

class MidiaSerializer(ModelSerializer):
    class Meta:
        model = Midia
        fields = "__all__"