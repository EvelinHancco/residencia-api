from django.contrib import admin
from .models.accesos import Accesos
from .models.apoderado import Apoderado
from .models.asistencia_evento import AsistenciaEvento
from .models.estado_permiso import EstadoPermiso
from .models.evento import Evento
from .models.habitacion import Habitacion
from .models.incidencia import Incidencia
from .models.interno_periodo import InternoPeriodo
from .models.interno_residencia import InternoResidencia
from .models.periodo_habitacion import PeriodoHabitacion
from .models.periodo_usuario import PeriodoUsuario
from .models.periodo import Periodo
from .models.permiso import Permiso
from .models.persona import Persona
from .models.privilegio import Privilegio
from .models.rol import Rol
from .models.tipo_evento import TipoEvento


@admin.register(Accesos)
class AccesosAdmin(admin.ModelAdmin):
    pass


@admin.register(Apoderado)
class ApoderadoAdmin(admin.ModelAdmin):
    pass


@admin.register(AsistenciaEvento)
class AsistenciaEventoAdmin(admin.ModelAdmin):
    pass


@admin.register(EstadoPermiso)
class EstadoPermisoAdmin(admin.ModelAdmin):
    pass


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    pass


@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    pass


@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    pass


@admin.register(InternoPeriodo)
class InternoPeriodoAdmin(admin.ModelAdmin):
    pass


@admin.register(InternoResidencia)
class InternoResidenciaAdmin(admin.ModelAdmin):
    pass


@admin.register(PeriodoHabitacion)
class PeriodoHabitacionAdmin(admin.ModelAdmin):
    pass


@admin.register(PeriodoUsuario)
class PeriodoUsuarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    pass


@admin.register(Permiso)
class PermisoAdmin(admin.ModelAdmin):
    pass


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    pass


@admin.register(Privilegio)
class PrivilegioAdmin(admin.ModelAdmin):
    pass


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoEvento)
class TipoEventoAdmin(admin.ModelAdmin):
    pass
