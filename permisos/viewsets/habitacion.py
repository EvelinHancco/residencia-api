from rest_framework import viewsets
from ..models.habitacion import Habitacion
from ..serializers.habitacion import HabitacionSerializer


class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer