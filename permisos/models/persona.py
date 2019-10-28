from django.db import models


class Persona(models.Model):
    id_persona = models.IntegerField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    # Field name made lowercase.
    dni = models.DecimalField(db_column='DNI', max_digits=8, decimal_places=0)
    codigo = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    estado = models.IntegerField()
    sexo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)

    class Meta:
        db_table = 'persona'
