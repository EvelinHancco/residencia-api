from rest_framework import viewsets
from ..models.periodo_usuario import PeriodoUsuario
from ..serializers.periodo_usuario import PeriodoUsuarioSerializer


class PeriodoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PeriodoUsuario.objects.all()
    serializer_class = PeriodoUsuarioSerializer