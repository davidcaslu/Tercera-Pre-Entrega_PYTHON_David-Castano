from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()
    comision = forms.IntegerField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField() 
    apellido = forms.CharField()
    identificacion = forms.IntegerField()
    comision = forms.IntegerField()
    email = forms.EmailField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    identificacion = forms.IntegerField()
    email = forms.EmailField()
    profesion = forms.CharField()
    edad = forms.IntegerField()

class EntregableFormulario(forms.Form):
    nombre = forms.CharField()
    fechaEntrega = forms.DateField()
    entregado = forms.BooleanField()

class RegistroFormulario(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.CharField(label="E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repite la contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
