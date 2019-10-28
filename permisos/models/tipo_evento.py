from django.db import models


class TipoEvento(models.Model):
    id_tipo_evento = models.IntegerField(primary_key=True, editable=False)
    nombre_evento = models.CharField(max_length=20)
    tipo = models.CharField(max_length=30)

    class Meta:
        db_table = 'tipo_evento'
