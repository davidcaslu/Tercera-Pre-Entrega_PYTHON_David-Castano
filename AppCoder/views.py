from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/index.html")

def registro (request):
    if request.method == "POST":
        miFormulario = RegistroFormulario(request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            return render (request, "AppCoder/index.html")
        
    else:
        miFormulario = RegistroFormulario()
    
    return render(request, "AppCoder/registro.html", {"miFormulario1":miFormulario})

def iniciarSesion(request):
    if request.method == "POST":
        miFormulario = AuthenticationForm(request, data = request.POST)
        if miFormulario.is_valid():
            usuario = miFormulario.cleaned_data.get("username")
            contrasena = miFormulario.cleaned_data.get("password")

            miUsuario = authenticate(username=usuario, password=contrasena)
            if miUsuario:
                login(request, miUsuario)
                mensaje = f"{miUsuario}"
                return render (request, "AppCoder/index.html", {"mensaje":mensaje})

        else:
            mensaje = f"Datos incorrectos. Vuelve a intentar"
            return render (request, "AppCoder/index.html", {"mensaje":mensaje})
        
    else:
        miFormulario = AuthenticationForm()
    
    return render(request, "AppCoder/iniciarSesion.html", {"miFormulario1":miFormulario})


def agregar_profesor(request):
    profe1 = Profesor(nombre = "David", apellido = "Castaño", identificacion = "123567", email = "davidcaslu@gmail.com", profesion = "Audiovisual", edad = 22)
    profe1.save()
    return HttpResponse("Hemos agregado a un profesor a la base de datos.")


def agregar_estudiante(request):

    estudiante1 = Estudiante(nombre = "David", apellido = "Castaño", comision = 1294)
    estudiante1.save()
    return HttpResponse("Hemos agregado a un estudiante a la base de datos.")

def estudiantes(request):
    listaEstudiantes = Estudiante.objects.all()
    return render(request, "AppCoder/verEstudiantes.html", {"listaEstudiantes":listaEstudiantes})

def profesores(request):
    listaProfes = Profesor.objects.all()
    return render(request, "AppCoder/verProfesores.html", {"listaProfes":listaProfes})

def entregables(request):
    listaEntregables = Entregable.objects.all()
    return render(request, "AppCoder/verEntregables.html", {"listaEntregables":listaEntregables})

def cursos(request):
    listaCursos = Curso.objects.all()
    return render(request, "AppCoder/verCursos.html", {"listaCursos":listaCursos})

"""
#crear estudiante con html
def crearEstudiantes(request): #Crear formulario con html
    if request.method == 'POST':
        estudiante = Estudiante (nombre= request.POST['nombre'], apellido=request.POST['apellido'], comision=request.POST['comision'], email=request.POST['email'])
        estudiante.save()
        return render(request, "AppCoder/crearEstudiantes.html")

    return render(request, "AppCoder/index.html")
"""

def crearEstudiantes(request): #crear formulario con django
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        if miFormulario.is_valid(): #valida que los datos estén bien
            infoDict = miFormulario.cleaned_data #la info del formulario se pasa a tipo diccionario
            estudiante1 = Estudiante(nombre=infoDict["nombre"], apellido=infoDict["apellido"], identificacion=infoDict["identificacion"], comision=infoDict["comision"], email=infoDict["email"])
            estudiante1.save()

        return render(request, "AppCoder/index.html")
    
    else:
        miFormulario = EstudianteFormulario()
    
    return render(request, "AppCoder/crearEstudiantes.html", {"formulario1": miFormulario})

def crearCursos(request): #crear formulario con django
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid(): #valida que los datos estén bien
            infoDict = miFormulario.cleaned_data #la info del formulario se pasa a tipo diccionario
            curso1 = Curso(nombre=infoDict["nombre"], camada=infoDict["camada"], comision=infoDict["comision"])
            curso1.save()

        return render(request, "AppCoder/index.html")
    
    else:
        miFormulario = CursoFormulario()
    
    return render(request, "AppCoder/crearCursos.html", {"formulario1": miFormulario})


def crearProfesor(request): 
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid(): #valida que los datos estén bien
            infoDict = miFormulario.cleaned_data #la info del formulario se pasa a tipo diccionario
            profesor1 = Profesor(nombre=infoDict["nombre"], apellido=infoDict["apellido"], identificacion=infoDict["identificacion"], email=infoDict["email"], profesion=infoDict["profesion"], edad=infoDict["edad"])
            profesor1.save()

        return render(request, "AppCoder/index.html")
    
    else:
        miFormulario = ProfesorFormulario()
    
    return render(request, "AppCoder/crearProfesor.html", {"formulario1": miFormulario})

def crearEntregable(request): 
    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)
        if miFormulario.is_valid(): #valida que los datos estén bien
            infoDict = miFormulario.cleaned_data #la info del formulario se pasa a tipo diccionario
            entregable1 = Entregable(nombre=infoDict["nombre"], fechaEntrega=infoDict["fechaEntrega"], entregado=infoDict["entregado"])
            entregable1.save()

        return render(request, "AppCoder/index.html")
    
    else:
        miFormulario = EntregableFormulario()
    
    return render(request, "AppCoder/crearEntregable.html", {"formulario1": miFormulario})


def buscarCamada(request):
    return render(request, "AppCoder/buscarCurso.html")

def buscarProfesor(request):
    return render(request, "AppCoder/buscarProfesor.html")

def buscarEstudiante(request):
    return render(request, "AppCoder/buscarEstudiante.html")

def buscarEntregable(request):
    return render(request, "AppCoder/buscarEntregable.html")

def resultadoBusquedaProfesor(request):

    if request.method == "GET":

        identificacionBusqueda = request.GET['identificacion']
        profesorResultados = Profesor.objects.filter(identificacion__icontains=identificacionBusqueda)
        if identificacionBusqueda != "":
            return render(request, "AppCoder/resultadoBusquedaProfesor.html", {"identificacion":identificacionBusqueda, "resultado": profesorResultados})

        elif identificacionBusqueda == "":
            respuesta = "No enviaste datos"
            return render(request, "AppCoder/resultadoBusquedaProfesorVacio.html", {"identificacion":respuesta, "resultado": respuesta})

    else:
        respuesta = "Raios"
        return HttpResponse(respuesta)


def resultadoBusquedaEstudiante(request):

    if request.method == "GET":

        identificacionBusqueda = request.GET['identificacion']
        estudianteResultados = Estudiante.objects.filter(identificacion__icontains=identificacionBusqueda)
        if identificacionBusqueda != "":
            return render(request, "AppCoder/resultadoBusquedaEstudiante.html", {"identificacion":identificacionBusqueda, "resultado":estudianteResultados})
        
        elif identificacionBusqueda == "":
            respuesta = "No enviaste datos"
            return render(request, "AppCoder/resultadoBusquedaEstudianteVacio.html", {"identificacion":respuesta, "resultado": respuesta})

    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)

def resultadoBusquedaCamada(request):

    if request.method == "GET":

        camadaBusqueda = request.GET['camada']
        cursosResultados = Curso.objects.filter(camada__icontains=camadaBusqueda)
        if camadaBusqueda != "":
            return render(request, "AppCoder/resultadoBusquedaCurso.html", {"camada":camadaBusqueda, "resultado":cursosResultados})
        
        elif camadaBusqueda == "":
            respuesta = "No enviaste datos"
            return render(request, "AppCoder/resultadoBusquedaCursoVacio.html", {"camada":respuesta, "resultado": respuesta})


    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)


def resultadoBusquedaEntregable(request):

    if request.method == "GET":

        nombreBusqueda = request.GET['nombre']
        entregableResultados = Entregable.objects.filter(nombre__icontains=nombreBusqueda)
        if nombreBusqueda != "":
            return render(request, "AppCoder/resultadoBusquedaEntregable.html", {"nombre":nombreBusqueda, "resultado":entregableResultados})

        elif nombreBusqueda == "":
            respuesta = "No enviaste datos"
            return render(request, "AppCoder/resultadoBusquedaEntregableVacio.html", {"nombre":respuesta, "resultado":respuesta})

    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)


def borrarProfesores(request, profesor_identificacion):
    profesor_elegido = Profesor.objects.get(identificacion = profesor_identificacion)
    profesor_elegido.delete()

    return render(request, "AppCoder/index.html")

def borrarEstudiantes(request, estudiante_identificacion):
    estudiante_elegido = Estudiante.objects.get(identificacion = estudiante_identificacion)
    estudiante_elegido.delete()

    return render(request, "AppCoder/index.html")

def borrarCursos(request, curso_camada):
    curso_elegido = Curso.objects.get(camada = curso_camada)
    curso_elegido.delete()

    return render(request, "AppCoder/index.html")

def borrarEntregable(request, entregable_nombre):
    entregable_elegido = Entregable.objects.get(nombre = entregable_nombre)
    entregable_elegido.delete()

    return render(request, "AppCoder/index.html")

def editarProfesor(request, profesor_identificacion):
    profesor_elegido=Profesor.objects.get(identificacion=profesor_identificacion)

    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid(): #valida que los datos estén bien
            infoDict = miFormulario.cleaned_data #la info del formulario se pasa a tipo diccionario
            profesor_elegido.nombre=infoDict["nombre"]
            profesor_elegido.apellido=infoDict["apellido"]
            profesor_elegido.identificacion=infoDict["identificacion"]
            profesor_elegido.email=infoDict["email"]
            profesor_elegido.profesion=infoDict["profesion"]
            profesor_elegido.edad=infoDict["edad"]

            profesor_elegido.save()

            return render(request, "AppCoder/index.html")

    else:
        miFormulario = ProfesorFormulario(initial={"nombre": profesor_elegido.nombre, "apellido": profesor_elegido.apellido, "identificacion": profesor_elegido.identificacion, "email": profesor_elegido.email, "profesion": profesor_elegido.profesion, "edad": profesor_elegido.edad})

    return render(request, "AppCoder/editarProfesor.html", {"formulario1": miFormulario})

def editarEstudiante(request, estudiante_identificacion):
    estudiante_elegido=Estudiante.objects.get(identificacion=estudiante_identificacion)

    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        if miFormulario.is_valid(): #valida que los datos estén bien
            infoDict = miFormulario.cleaned_data #la info del formulario se pasa a tipo diccionario
            estudiante_elegido.nombre=infoDict["nombre"]
            estudiante_elegido.apellido=infoDict["apellido"]
            estudiante_elegido.identificacion=infoDict["identificacion"]
            estudiante_elegido.comision =infoDict["comision"]
            estudiante_elegido.email=infoDict["email"]

            estudiante_elegido.save()

            return render(request, "AppCoder/index.html")

    else:
        miFormulario = EstudianteFormulario(initial={"nombre": estudiante_elegido.nombre, "apellido": estudiante_elegido.apellido, "identificacion": estudiante_elegido.identificacion, "comision": estudiante_elegido.comision,"email": estudiante_elegido.email})

    return render(request, "AppCoder/editarEstudiante.html", {"formulario1": miFormulario})

def editarCurso(request, curso_camada):
    curso_elegido=Curso.objects.get(camada=curso_camada)

    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid(): #valida que los datos estén bien
            infoDict = miFormulario.cleaned_data #la info del formulario se pasa a tipo diccionario
            curso_elegido.nombre=infoDict["nombre"]
            curso_elegido.camada=infoDict["camada"]
            curso_elegido.comision =infoDict["comision"]

            curso_elegido.save()

            return render(request, "AppCoder/index.html")

    else:
        miFormulario = CursoFormulario(initial={"nombre": curso_elegido.nombre, "camada": curso_elegido.camada, "comision": curso_elegido.comision})

    return render(request, "AppCoder/editarCurso.html", {"formulario1": miFormulario})

def editarEntregable(request, entregable_nombre):
    entregable_elegido=Entregable.objects.get(nombre=entregable_nombre)

    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)
        if miFormulario.is_valid(): #valida que los datos estén bien
            infoDict = miFormulario.cleaned_data #la info del formulario se pasa a tipo diccionario
            entregable_elegido.nombre=infoDict["nombre"]
            entregable_elegido.fechaEntrega=infoDict["fechaEntrega"]
            entregable_elegido.entregado =infoDict["entregado"]

            entregable_elegido.save()

            return render(request, "AppCoder/index.html")

    else:
        miFormulario = EntregableFormulario(initial={"nombre": entregable_elegido.nombre, "fechaEntrega": entregable_elegido.fechaEntrega, "entregado": entregable_elegido.entregado})

    return render(request, "AppCoder/editarEntregable.html", {"formulario1": miFormulario})

class CursoLista (ListView):
    model = Curso
    template_name= "AppCoder/verCursos_clase.html"

class CursoCrear (LoginRequiredMixin, CreateView,):
    model = Curso
    fields = ["nombre", "camada", "comision"]
    template_name = "AppCoder/crearCursos_clase.html"
    success_url = "/AppCoder/cursos/clase"

class CursoBorrar (LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = "AppCoder/borrarCursos_clase.html"
    success_url = "/AppCoder/cursos/clase"
    #Tiene un problema y es que toca poner el ID del curso en la url del navegador

class CursoEditar (LoginRequiredMixin, UpdateView):
    model = Curso
    fields = ["nombre", "camada", "comision"]
    success_url = "/AppCoder/cursos/clase"
    #Tiene un problema y es que toca poner el ID del curso en la url del navegador, no es muy claro cual se está eliminando