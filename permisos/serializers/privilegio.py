from rest_framework import serializers
from ..models.privilegio import Privilegio


class PrivilegioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privilegio
        fields = '__all__'

