from django.db import models


class Periodo(models.Model):
    id_periodo = models.IntegerField(primary_key=True, editable=False)
    fecha_inicio = models.DateField()
    nombre_periodo = models.CharField(max_length=20)
    fecha_fin = models.DateField()
    estado = models.IntegerField()
    descripcion = models.CharField(max_length=30)

    class Meta:
        db_table = 'periodo'
