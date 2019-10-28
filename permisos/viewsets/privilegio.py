from rest_framework import viewsets
from ..models.privilegio import Privilegio
from ..serializers.privilegio import PrivilegioSerializer


class PrivilegioViewSet(viewsets.ModelViewSet):
    queryset = Privilegio.objects.all()
    serializer_class = PrivilegioSerializer