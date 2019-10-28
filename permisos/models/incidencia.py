from django.db import models


class Incidencia(models.Model):
    id_incidencia = models.IntegerField(primary_key=True, editable=False)
    descripcion = models.CharField(max_length=50)
    fecha_incidencia = models.DateField()
    estado = models.IntegerField()
    id_periodo_usuario = models.ForeignKey(
        'PeriodoUsuario', models.CASCADE, db_column='id_periodo_usuario')

    class Meta:
        db_table = 'incidencia'
