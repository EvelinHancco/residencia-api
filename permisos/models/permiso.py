from django.db import models


class Permiso(models.Model):
    id_permiso = models.IntegerField(primary_key=True, editable=False)
    motivo = models.CharField(max_length=50)
    fecha_estimada_salida = models.DateField()
    fecha_estimada_entrada = models.DateField()
    lugar = models.CharField(max_length=30)
    observaciones = models.CharField(max_length=50)
    id_interno_periodo = models.ForeignKey(
        'InternoPeriodo', models.CASCADE, db_column='id_interno_periodo')
    id_persona = models.CharField(max_length=20)

    class Meta:
        db_table = 'permiso'
