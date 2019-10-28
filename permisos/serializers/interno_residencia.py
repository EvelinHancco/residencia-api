from rest_framework import serializers
from ..models.interno_residencia import InternoResidencia


class InternoResidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternoResidencia
        fields = '__all__'

