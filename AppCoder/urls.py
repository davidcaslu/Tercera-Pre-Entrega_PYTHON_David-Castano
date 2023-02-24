from django.urls import path
from AppCoder.views import * #importa todo
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #Genéricos
    path('', inicio, name='Start'),
    path('inicio', inicio, name='Start'),
    path('accounts/login/', iniciarSesion, name='iniciar sesion login'),

    path('registro', registro, name='registro'),
    path('iniciarSesion', iniciarSesion, name='iniciar sesion'),
    path('logOut', LogoutView.as_view(template_name="AppCoder/logout.html"), name='cerrar sesion'),

    #Ver
    path('verEstudiantes', estudiantes, name='Estudiantes'),
    path('verProfesores', profesores, name='Profesores'),
    path('verEntregables', entregables, name='Entregables'),
    path('verCursos', cursos, name='Cursos'),

    #crear
    path('crearEstudiantes', crearEstudiantes, name='crearEstudiantes'),
    path('crearCursos', crearCursos, name='crearCursos'),
    path('crearProfesor', crearProfesor, name='crearProfesor'),
    path('crearEntregable', crearEntregable, name='crearEntregable'),

    #buscar
    path('buscarEstudiante', buscarEstudiante, name='buscarEstudiante'),
    path('buscarCurso', buscarCamada, name='buscarCurso'),
    path('buscarProfesor', buscarProfesor, name='buscarProfesor'),
    path('buscarEntregable', buscarEntregable, name='buscarEntregable'),

    path('resultadoBusquedaCurso', resultadoBusquedaCamada, name='resultadoBusquedaCurso'),
    path('resultadoBusquedaProfesor', resultadoBusquedaProfesor, name='resultadoBusquedaProfesor'),
    path('resultadoBusquedaEstudiante', resultadoBusquedaEstudiante, name='resultadoBusquedaEstudiante'),
    path('resultadoBusquedaEntregable', resultadoBusquedaEntregable, name='resultadoBusquedaEntregable'),

    #borrar
    path('borrarProfesores/<profesor_identificacion>', borrarProfesores, name='borrarProfesores'),
    path('borrarEstudiantes/<estudiante_identificacion>', borrarEstudiantes, name='borrarEstudiantes'),
    path('borrarCurso/<curso_camada>', borrarCursos, name='borrarCursos'),
    path('borrarEntregable/<entregable_identificador>', borrarEntregable, name='borrarEntregables'),

    #editar
    path('editarProfesor/<profesor_identificacion>', editarProfesor, name='editarProfesor'),
    path('editarEstudiante/<estudiante_identificacion>', editarEstudiante, name='editarEstudiante'),
    path('editarCurso/<curso_camada>', editarCurso, name='editarCurso'),
    path('editarEntregable/<entregable_identificador>', editarEntregable, name='editarEntregable'),

]
