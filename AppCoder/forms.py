from django import forms

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
