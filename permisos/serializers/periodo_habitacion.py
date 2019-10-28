from rest_framework import serializers
from ..models.periodo_habitacion import PeriodoHabitacion


class PeriodoHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodoHabitacion
        fields = '__all__'

