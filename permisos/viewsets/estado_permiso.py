from rest_framework import viewsets
from ..models.estado_permiso import EstadoPermiso
from ..serializers.estado_permiso import EstadoPermisoSerializer


class EstadoPermisoViewSet(viewsets.ModelViewSet):
    queryset = EstadoPermiso.objects.all()
    serializer_class = EstadoPermisoSerializer