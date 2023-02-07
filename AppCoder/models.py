from django.db import models

# Create your models here.

class Estudiante(models.Model):
    #debido al modelo models.Model no es necesario iniciar con __init__
    nombre = models.CharField(max_length=40) #models.CharField permite crear campos de solo texto y hay que indicar qué tantos caracteres
    apellido = models.CharField(max_length=40)
    comision = models.IntegerField(default=0) #models.IntegerField permite crear campos de solo números
    email = models.EmailField(default=None)
    #fecha = models.DateField() #models.DateField un campo de tipo fecha

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)
    edad = models.IntegerField(default = 0)

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    comision = models.IntegerField()