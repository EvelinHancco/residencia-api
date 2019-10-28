from rest_framework import serializers
from ..models.accesos import Accesos


class AccesosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accesos
        fields = '__all__'
