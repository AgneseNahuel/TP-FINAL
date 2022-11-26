from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Doom.models import *
from .forms import *

# Create your views here.
def inicio(request):
    return render (request, "inicio.html")

def formularioAutor(request):
    return render(request, "formularioAutor.html")

def formularioJuego(request):
    return render(request, "formularioJuego.html")

def formularioCancion(request):
    
    if request.method=="POST":
        form=formularioC(request.POST)
        print(form)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombreb= informacion["nombre"]
            duracionb= informacion["duracion"]
            fechadesalidab= informacion["fechadesalida"]


            busqueda1=Cancion(nombre=nombreb, duracion=duracionb, fechadesalida=fechadesalidab)
            busqueda1.save()
            return render (request, "inicio.html")
    else:
        formulario=formularioC()

    return render(request, "formularioCancion.html", {"form":formulario})