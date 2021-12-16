from django.shortcuts import render

from django.http import HttpResponse

from AppCoder.models import Estadio, Liga

# Create your views here.

#Formularios
def estadioFormulario(request):
    
    #obtiene los valores
    if request.method == "POST":
        
        estadio = Estadio( nombre = request.POST['nombre'], capacidad = request.POST['capacidad'], direccion = request.POST['direccion'], anioFundacion = request.POST['anioFundacion'] )
        
        estadio.save()
        
        return render(request, 'AppCoder/inicio.html')
        
    
    return render(request, 'AppCoder/estadioFormulario.html')

def ligaFormulario(request):
    
    #obtiene los valores
    if request.method == "POST":
        
        liga = Liga( nombre = request.POST['nombre'], cantidadDeEquipos = request.POST['cantidadDeEquipos'], pais = request.POST['pais'])
        
        liga.save()
        
        return render(request, 'AppCoder/inicio.html')
        
    
    return render(request, 'AppCoder/ligaFormulario.html')

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

