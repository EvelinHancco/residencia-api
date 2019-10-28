from rest_framework import routers
from .viewsets.accesos import AccesosViewSet
from .viewsets.apoderado import ApoderadoViewSet
from .viewsets.asistencia_evento import AsistenciaEventoViewSet
from .viewsets.estado_permiso import EstadoPermisoViewSet
from .viewsets.evento import EventoViewSet
from .viewsets.habitacion import HabitacionViewSet
from .viewsets.incidencia import IncidenciaViewSet
from .viewsets.interno_periodo import InternoPeriodoViewSet
from .viewsets.interno_residencia import InternoResidenciaViewSet
from .viewsets.periodo_habitacion import PeriodoHabitacionViewSet
from .viewsets.periodo_usuario import PeriodoUsuarioViewSet
from .viewsets.periodo import PeriodoViewSet
from .viewsets.permiso import PermisoViewSet
from .viewsets.persona import PersonaViewSet
from .viewsets.privilegio import PrivilegioViewSet
from .viewsets.rol import RolViewSet
from .viewsets.tipo_evento import TipoEventoViewSet


from django.urls import path, include
router = routers.DefaultRouter()

router.register(r'accesos', AccesosViewSet)
router.register(r'apoderados', ApoderadoViewSet)
router.register(r'asistencias-eventos', AsistenciaEventoViewSet)
router.register(r'eventos', EventoViewSet)
router.register(r'habitaciones', HabitacionViewSet)
router.register(r'incidencias', IncidenciaViewSet)
router.register(r'interno-periodo', InternoPeriodoViewSet)
router.register(r'interno-residencia', InternoResidenciaViewSet)
router.register(r'periodo-habitaciones', PeriodoHabitacionViewSet)
router.register(r'periodo-usuarios', PeriodoUsuarioViewSet)
router.register(r'periodos', PeriodoViewSet)
router.register(r'permisos', PermisoViewSet)
router.register(r'personas', PersonaViewSet)
router.register(r'privilegios', PrivilegioViewSet)
router.register(r'roles', RolViewSet)
router.register(r'tipo-eventos', TipoEventoViewSet)

urlpatterns = [
    path('',  include(router.urls)),
]
