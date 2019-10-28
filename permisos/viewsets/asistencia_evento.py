from rest_framework import viewsets
from ..models.asistencia_evento import AsistenciaEvento
from ..serializers.asistencia_evento import AsistenciaEventoSerializer


class AsistenciaEventoViewSet(viewsets.ModelViewSet):
    queryset = AsistenciaEvento.objects.all()
    serializer_class = AsistenciaEventoSerializer
