from django.db import models


class PeriodoUsuario(models.Model):
    id_periodo_usuario = models.IntegerField(primary_key=True, editable=False)
    id_rol = models.ForeignKey('Rol', models.CASCADE, db_column='id_rol')
    id_periodo = models.ForeignKey(
        'Periodo', models.CASCADE, db_column='id_periodo')
    id_persona = models.ForeignKey(
        'Persona', models.CASCADE, db_column='id_persona')

    class Meta:
        db_table = 'periodo_usuario'
