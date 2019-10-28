from rest_framework import viewsets
from ..models.incidencia import Incidencia
from ..serializers.incidencia import IncidenciaSerializer


class IncidenciaViewSet(viewsets.ModelViewSet):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer