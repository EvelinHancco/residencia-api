from rest_framework import viewsets
from ..models.apoderado import Apoderado
from ..serializers.apoderado import ApoderadoSerializer

class ApoderadoViewSet(viewsets.ModelViewSet):
    queryset = Apoderado.objects.all()
    serializer_class = ApoderadoSerializer
