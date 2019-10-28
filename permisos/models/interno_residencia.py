from django.db import models


class InternoResidencia(models.Model):
    id_interno_residencia = models.IntegerField(primary_key=True, editable=False)
    nombre_residencia = models.CharField(max_length=30)

    class Meta:
        db_table = 'interno_residencia'
