from rest_framework import viewsets
from ..models.interno_residencia import InternoResidencia
from ..serializers.interno_residencia import InternoResidenciaSerializer


class InternoResidenciaViewSet(viewsets.ModelViewSet):
    queryset = InternoResidencia.objects.all()
    serializer_class = InternoResidenciaSerializer