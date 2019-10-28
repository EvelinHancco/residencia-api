from django.db import models


class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True, editable=False)
    nombre_rol = models.CharField(max_length=30)
    tipo = models.CharField(max_length=20)
    descripcion_rol = models.CharField(max_length=50)

    class Meta:
        db_table = 'rol'
