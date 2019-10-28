from rest_framework import serializers
from ..models.asistencia_evento import AsistenciaEvento


class AsistenciaEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsistenciaEvento
        fields = '__all__'