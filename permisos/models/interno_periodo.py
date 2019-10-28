from django.db import models


class InternoPeriodo(models.Model):
    id_interno_periodo = models.IntegerField(primary_key=True, editable=False)
    id_apoderado = models.ForeignKey(
        'Apoderado', models.CASCADE, db_column='id_apoderado')
    id_periodo = models.ForeignKey(
        'Periodo', models.CASCADE, db_column='id_periodo')
    id_periodo_habitacion = models.ForeignKey(
        'PeriodoHabitacion', models.CASCADE, db_column='id_periodo_habitacion')

    class Meta:
        db_table = 'interno_periodo'
