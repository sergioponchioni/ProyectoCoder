from django import forms

class EstadioFormulario(forms.Form):
    
    #Campos
    nombre = forms.CharField(required=True)
    
    capacidad = forms.IntegerField()
    
    direccion = forms.CharField()
    
    anioFundacion = forms.IntegerField(max_value=2021)
    
class ArbitroFormulario(forms.Form):
    
    nombre = forms.CharField(required=True)
    
    nacionalidad = forms.CharField(required=True)
    
    edad = forms.IntegerField()
    
class SeleccionFormulario(forms.Form):
    
    nombre = forms.CharField(required=True)
    
    tecnico = forms.CharField(required=True)
    
    continente = forms.CharField(required=True)
    
class LigaFormulario(forms.Form):
    
    nombre = forms.CharField(required=True)
    
    cantidadDeEquipos = forms.IntegerField()
    
    pais = forms.CharField(required=True)