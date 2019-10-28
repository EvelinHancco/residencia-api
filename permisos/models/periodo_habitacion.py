from django.db import models


class PeriodoHabitacion(models.Model):
    id_periodo_habitacion = models.IntegerField(primary_key=True, editable=False)
    id_periodo = models.ForeignKey(
        'Periodo', models.CASCADE, db_column='id_periodo')
    id_habitacion = models.ForeignKey(
        'Habitacion', models.CASCADE, db_column='id_habitacion')

    class Meta:
        db_table = 'periodo_habitacion'
