from django.shortcuts import render
from .models import Games_Data

# Create your views here.


def home(request):
    game = Games_Data.objects.all()
    return render(request, "home.html", {"game": game})
