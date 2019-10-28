from rest_framework import viewsets
from ..models.periodo_habitacion import PeriodoHabitacion
from ..serializers.periodo_habitacion import PeriodoHabitacionSerializer


class PeriodoHabitacionViewSet(viewsets.ModelViewSet):
    queryset = PeriodoHabitacion.objects.all()
    serializer_class = PeriodoHabitacionSerializer