from rest_framework import serializers
from ..models.estado_permiso import EstadoPermiso


class EstadoPermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPermiso
        fields = '__all__'
