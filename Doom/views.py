from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Doom.models import *
from .forms import *

# Create your views here.
def inicio(request):
    return render (request, "inicio.html")

def formularioAutor(request):
    if request.method=="POST":
        form=formularioA(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            edad=informacion["edad"]
            fechadenacimiento=informacion["fechadenacimiento"]
            
            busqueda=Autor(nombre=nombre, edad=edad, fechadenacimiento=fechadenacimiento)
            busqueda.save()
            return render (request, "inicio.html", {"mensaje":"se creo bien"})
        else:
            formulario=formularioA
        return render(request, "formularioAutor.html", {"form":formulario})

    return render(request, "formularioAutor.html")

def formularioJuego(request):
    if request.method=="POST":
        form=formularioJ(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombreV=informacion["nombre"]
            duracionV=informacion["duracion"]
            fechadesalidaV=informacion["fechadesalida"]

            busqueda2=Juego(nombre=nombreV, duracion=duracionV, fechadesalida=fechadesalidaV)
            busqueda2.save()
            return render (request, "inicio.html", {"mensaje":"se creo bien"})
    else:
        formulario=formularioJ()

    return render(request, "formularioJuego.html", {"form":formulario})

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

#esta es la vista para buscar
def busquedac(request):
    return render(request, "busquedac.html")

def buscarc(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        nombrec=Cancion.objects.filter(nombre__icontains=nombre)
        return render(request, "resultadocancion.html", {"nombrec":nombrec})
    else:
        return render(request, "busquedac.html", {"mensaje":"NO VALIDO"})
