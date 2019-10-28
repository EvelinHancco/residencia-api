from django.db import models


class Accesos(models.Model):
    id_accesos = models.IntegerField(primary_key=True, editable=False)
    url = models.CharField(max_length=150)

    class Meta:
        db_table = 'accesos'
