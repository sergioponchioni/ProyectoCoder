from django.urls import path #Importamos el path
from AppCoder import views # Importamos las vistas

urlpatterns = [
    path('inicio/', views.inicio),
    path('jugadores/', views.jugadores),
]
