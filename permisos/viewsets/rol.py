from rest_framework import viewsets
from ..models.rol import Rol
from ..serializers.rol import RolSerializer


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer