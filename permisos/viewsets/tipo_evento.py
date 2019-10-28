from rest_framework import viewsets
from ..models.tipo_evento import TipoEvento
from ..serializers.tipo_evento import TipoEventoSerializer


class TipoEventoViewSet(viewsets.ModelViewSet):
    queryset = TipoEvento.objects.all()
    serializer_class = TipoEventoSerializer