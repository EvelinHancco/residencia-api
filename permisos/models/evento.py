from django.db import models


class Evento(models.Model):
    id_evento = models.IntegerField(primary_key=True, editable=False)
    lugar = models.CharField(max_length=20)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    id_tipo_evento = models.ForeignKey(
        'TipoEvento', models.CASCADE, db_column='id_tipo_evento')
    id_periodo_usuario = models.ForeignKey(
        'PeriodoUsuario', models.CASCADE, db_column='id_periodo_usuario')

    class Meta:
        db_table = 'evento'
