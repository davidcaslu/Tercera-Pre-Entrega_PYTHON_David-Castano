from django.urls import path
from AppCoder.views import * #importa todo

urlpatterns = [
    path('', inicio, name='Start'),
    path('inicio', inicio, name='Start'),
    path('agregar_profe', agregar_profesor),
    path('agregar_estudiante', agregar_estudiante),
    path('verEstudiantes', estudiantes, name='Estudiantes'),
    path('verProfesores', profesores, name='Profesores'),
    path('verEntregables', entregables, name='Entregables'),
    path('verCursos', cursos, name='Cursos'),

    path('crearEstudiantes', crearEstudiantes, name='crearEstudiantes'),
    path('crearCursos', crearCursos, name='crearCursos'),
    path('crearProfesor', crearProfesor, name='crearProfesor'),
    path('crearEntregable', crearEntregable, name='crearEntregable'),

    path('buscarEstudiante', buscarEstudiante, name='buscarEstudiante'),
    path('buscarCamada', buscarCamada, name='buscarCamada'),
    path('buscarProfesor', buscarProfesor, name='buscarProfesor'),
    path('buscarEntregable', buscarEntregable, name='buscarEntregable'),

    path('resultadoBusquedaCamada', resultadoBusquedaCamada, name='resultadoBusquedaCamada'),
    path('resultadoBusquedaProfesor', resultadoBusquedaProfesor, name='resultadoBusquedaProfesor'),
    path('resultadoBusquedaEstudiante', resultadoBusquedaEstudiante, name='resultadoBusquedaEstudiante'),
    path('resultadoBusquedaEntregable', resultadoBusquedaEntregable, name='resultadoBusquedaEntregable'),
]
