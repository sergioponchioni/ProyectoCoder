from django.shortcuts import render

from django.http import HttpResponse

from AppCoder.models import Estadio, Liga, Arbitro, Seleccion
from AppCoder.forms import EstadioFormulario, ArbitroFormulario, SeleccionFormulario, LigaFormulario

# Create your views here.

def seleccionFormulario(request):
    
    #obtiene los valores
    if request.method == "POST":
        
        miFormulario = SeleccionFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
        
            seleccion = Seleccion( nombre = informacion['nombre'], continente = informacion['continente'], tecnico = informacion['tecnico'] )
            
            seleccion.save()
            
            return render(request, 'AppCoder/inicio.html')
    
    else:
        
        miFormulario = SeleccionFormulario()
    
    return render(request, 'AppCoder/seleccionFormulario.html', {"miFormulario": miFormulario})


#Formularios
def estadioFormulario(request):
    
    #obtiene los valores
    if request.method == "POST":
        
        miFormulario = EstadioFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
        
            estadio = Estadio( nombre = informacion['nombre'], capacidad = informacion['capacidad'], direccion = informacion['direccion'], anioFundacion = informacion['anioFundacion'] )
            
            estadio.save()
            
            return render(request, 'AppCoder/inicio.html')
    
    else:
        
        miFormulario = EstadioFormulario()
        
    
    return render(request, 'AppCoder/estadioFormulario.html', {"miFormulario": miFormulario})

def ligaFormulario(request):
    
    #obtiene los valores
    if request.method == "POST":
        
        miFormulario = LigaFormulario(request.POST)
        
        if miFormulario.is_valid():
                
            informacion = miFormulario.cleaned_data
        
            liga = Liga( nombre = informacion['nombre'], cantidadDeEquipos = informacion['cantidadDeEquipos'], pais = informacion['pais'])
            
            liga.save()
            
            return render(request, 'AppCoder/inicio.html')
    else:
        
        miFormulario = LigaFormulario()   
    
    return render(request, 'AppCoder/ligaFormulario.html', {"miFormulario": miFormulario})

def arbitroFormulario(request):
    
    #obtiene los valores
    if request.method == "POST":
        
        miFormulario = ArbitroFormulario(request.POST)
        
        if miFormulario.is_valid():
                
            informacion = miFormulario.cleaned_data
            
            arbitro = Arbitro( nombre = informacion['nombre'], nacionalidad = informacion['nacionalidad'], edad = informacion['edad'] )
            
            arbitro.save()
            
            return render(request, 'AppCoder/inicio.html')
        
    else:
        
        miFormulario = ArbitroFormulario()
        
    
    return render(request, 'AppCoder/arbitroFormulario.html', {"miFormulario": miFormulario})
#Primer vista
def inicio(request):
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/inicio.html')

def jugadores(request):
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/jugadores.html')

def equipos(request):
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/equipos.html')

def estadios(request):
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/estadios.html')

def ligas(request):
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/ligas.html')

def arbitros(request):
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/arbitros.html')

def selecciones(request):
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/selecciones.html')

