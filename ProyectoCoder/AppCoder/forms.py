from django import forms

class EstadioFormulario(forms.Form):
    
    #Campos
    nombre = forms.CharField(required=True)
    
    capacidad = forms.IntegerField()
    
    direccion = forms.CharField()
    
    anioFundacion = forms.IntegerField()