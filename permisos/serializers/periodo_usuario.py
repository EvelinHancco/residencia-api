from rest_framework import serializers
from ..models.periodo_usuario import PeriodoUsuario


class PeriodoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodoUsuario
        fields = '__all__'

