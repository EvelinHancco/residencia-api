from django.db import models


class AsistenciaEvento(models.Model):
    id_reporte_evento = models.IntegerField(primary_key=True, editable=False)
    estado = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    id_interno_periodo = models.ForeignKey(
        'InternoPeriodo', models.CASCADE, db_column='id_interno_periodo')
    id_evento = models.ForeignKey(
        'Evento', models.CASCADE, db_column='id_evento')
    id_persona = models.ForeignKey(
        'Persona', models.CASCADE, db_column='id_persona')

    class Meta:
        db_table = 'asistencia_evento'
