from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    identificacion = models.IntegerField(default=0)
    comision = models.IntegerField(default=0)
    email = models.EmailField(default=None)

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    identificacion = models.IntegerField(default=0)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)
    edad = models.IntegerField(default = 0)

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    identificador = models.IntegerField(default=0)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    comision = models.IntegerField()

class AvatarImagen(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
