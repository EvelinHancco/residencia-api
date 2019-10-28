from rest_framework import viewsets
from ..models.accesos import Accesos
from ..serializers.accesos import AccesosSerializer

class AccesosViewSet(viewsets.ModelViewSet):
    queryset = Accesos.objects.all()
    serializer_class = AccesosSerializer
