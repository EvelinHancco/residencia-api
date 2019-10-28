from django.db import models


class Apoderado(models.Model):
    id_apoderado = models.IntegerField(primary_key=True, editable=False)
    parentesco = models.CharField(max_length=30)

    class Meta:
        db_table = 'apoderado'
