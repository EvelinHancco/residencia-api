from django.db import models


class EstadoPermiso(models.Model):
    id_estado_permiso = models.IntegerField(primary_key=True, editable=False)
    id_permiso = models.ForeignKey(
        'Permiso', models.CASCADE, db_column='id_permiso')
    fecha_operacion = models.DateField()
    estado = models.DecimalField(max_digits=10, decimal_places=0)
    fecha_salida = models.DateField()
    fecha_entrada = models.DateField()
    falta_postpermiso = models.CharField(max_length=30)
    id_periodo_usuario = models.ForeignKey(
        'PeriodoUsuario', models.CASCADE, db_column='id_periodo_usuario')

    class Meta:
        db_table = 'estado_permiso'
