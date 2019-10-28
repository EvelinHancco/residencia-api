from rest_framework import serializers
from ..models.tipo_evento import TipoEvento


class TipoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEvento
        fields = '__all__'

