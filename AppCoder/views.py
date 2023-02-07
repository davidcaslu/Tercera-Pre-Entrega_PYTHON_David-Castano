from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/index.html")

def agregar_profesor(request):

    profe1 = Profesor(nombre = "David", apellido = "Castaño", email = "davidcaslu@gmail.com", profesion = "Audiovisual", edad = 22)
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
            curso1 = Estudiante(nombre=infoDict["nombre"], apellido=infoDict["apellido"], comision=infoDict["comision"], email=infoDict["email"])
            curso1.save()

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
            profesor1 = Profesor(nombre=infoDict["nombre"], apellido=infoDict["apellido"], email=infoDict["email"], profesion=infoDict["profesion"], edad=infoDict["edad"])
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
    return render(request, "AppCoder/buscarCamada.html")

def buscarProfesor(request):
    return render(request, "AppCoder/buscarProfesor.html")

def buscarEstudiante(request):
    return render(request, "AppCoder/buscarEstudiante.html")

def buscarEntregable(request):
    return render(request, "AppCoder/buscarEntregable.html")

def resultadoBusquedaProfesor(request):

    if request.method == "GET":

        nombreBusqueda = request.GET['nombre']
        profesorResultados = Profesor.objects.filter(nombre__icontains=nombreBusqueda)
        

        return render(request, "AppCoder/resultadoBusquedaProfesor.html", {"nombre":nombreBusqueda, "resultado": profesorResultados})

    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)


def resultadoBusquedaEstudiante(request):

    if request.method == "GET":

        nombreBusqueda = request.GET['nombre']
        estudianteResultados = Estudiante.objects.filter(nombre__icontains=nombreBusqueda)

        return render(request, "AppCoder/resultadoBusquedaEstudiante.html", {"nombre":nombreBusqueda, "resultado":estudianteResultados})

    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)

def resultadoBusquedaCamada(request):

    if request.method == "GET":

        camadaBusqueda = request.GET['camada']
        cursosResultados = Curso.objects.filter(camada__icontains=camadaBusqueda)

        return render(request, "AppCoder/resultadoBusquedaCamada.html", {"camada":camadaBusqueda, "resultado":cursosResultados})

    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)


def resultadoBusquedaEntregable(request):

    if request.method == "GET":

        nombreBusqueda = request.GET['nombre']
        entregableResultados = Entregable.objects.filter(nombre__icontains=nombreBusqueda)

        return render(request, "AppCoder/resultadoBusquedaEntregable.html", {"nombre":nombreBusqueda, "resultado":entregableResultados})

    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)