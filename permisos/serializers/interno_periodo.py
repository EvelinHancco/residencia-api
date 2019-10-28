from rest_framework import serializers
from ..models.interno_periodo import InternoPeriodo


class InternoPeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternoPeriodo
        fields = '__all__'
