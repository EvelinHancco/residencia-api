from rest_framework import viewsets
from ..models.interno_periodo import InternoPeriodo
from ..serializers.interno_periodo import InternoPeriodoSerializer


class InternoPeriodoViewSet(viewsets.ModelViewSet):
    queryset = InternoPeriodo.objects.all()
    serializer_class = InternoPeriodoSerializer