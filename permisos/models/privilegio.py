from django.db import models


class Privilegio(models.Model):
    id_privilegio = models.IntegerField(primary_key=True, editable=False)
    tipo_privilegio = models.CharField(max_length=20, blank=True, null=True)
    id_persona = models.ForeignKey(
        'Persona', models.CASCADE, db_column='id_persona')
    id_accesos = models.ForeignKey(
        'Accesos', models.CASCADE, db_column='id_accesos')

    class Meta:
        db_table = 'privilegio'
