from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("videojuego/<int:id>/", views.detalles_juegos, name="detalles_juegos"),
    path("videojuego/<int:id>/votar/", views.votar_positivo, name="votar_positivo"),
    path("videojuego/<int:id>/votar/", views.votar_negativo, name="votar_negativo"),
    path("buscar/", views.buscar_juegos, name="buscar_juegos"),
]
