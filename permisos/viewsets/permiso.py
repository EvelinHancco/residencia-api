from rest_framework import viewsets
from ..models.permiso import Permiso
from ..serializers.permiso import PermisoSerializer


class PermisoViewSet(viewsets.ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer