from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse
from django.db import IntegrityError
from .models import Games_Data, Users
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.


def home(request):
    game = Games_Data.objects.all()
    return render(request, "home.html", {"game": game})


def registro(request):
    if request.method == "GET":
        return render(request, "registro.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(
                    request,
                    "registro.html",
                    {"form": UserCreationForm, "error": "El usuario ya existe"},
                )
        return render(
            request,
            "registro.html",
            {"form": UserCreationForm, "error": "Las contraseñas no coinciden"},
        )


def buscar_juegos(request):
    query = request.GET.get("q")
    juegos = Games_Data.objects.filter(title__icontains=query) if query else []
    return render(request, "buscar_juegos.html", {"juegos": juegos, "query": query})


def bienvenida(request):
    return render(request, "bienvenida.html")


def detalles_juegos(request, id):
    juego = get_object_or_404(Games_Data.objects.all(), id=id)
    return render(request, "detalles_juego.html", {"juego": juego})


def votar_positivo(request, id):
    videojuego = get_object_or_404(Games_Data, id=id)
    videojuego.votes += 1  # O la lógica que uses para votar
    videojuego.save()
    return redirect("detalles_juegos", id=id)


def votar_negativo(request, id):
    videojuego = get_object_or_404(Games_Data, id=id)
    if videojuego.id > 0:
        videojuego.votes -= 1  # O la lógica que uses para votar
        videojuego.save()
    return redirect("detalles_juegos", id=id)


9
