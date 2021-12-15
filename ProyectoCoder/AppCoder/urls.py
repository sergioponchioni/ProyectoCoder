from django.urls import path #Importamos el path
from AppCoder import views # Importamos las vistas

urlpatterns = [
    
    path('inicio/', views.inicio, name="Inicio"),
    path('jugadores/', views.jugadores, name="Jugadores"),
    path('equipos/', views.equipos, name="Equipos"),
    path('estadios/', views.estadios, name="Estadios"),

]
