from django.db import models


class Habitacion(models.Model):
    id_habitacion = models.IntegerField(primary_key=True, editable=False)
    pabellon = models.CharField(max_length=10)
    capacidad = models.CharField(max_length=10)
    n_habitacion = models.CharField(max_length=10)
    id_interno_residencia = models.ForeignKey(
        'InternoResidencia', models.CASCADE, db_column='id_interno_residencia')

    class Meta:
        db_table = 'habitacion'
