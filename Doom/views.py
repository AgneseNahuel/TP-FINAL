from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Doom.models import *
from .forms import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


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

#Crud CANCION
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

#CRUD CANCION!!

def leerCanciones(request):
    canciones=Cancion.objects.all()
    return render(request, "LeerCancion.html", {"canciones": canciones})


def eliminarCanciones(request, id):
    cancion=Cancion.objects.get(id=id)
    cancion.delete()
    canciones=Cancion.objects.all()
    return render(request, "LeerCancion.html", {"mensaje":"CANCION ELIMINADA", "canciones":canciones})


def editarCancion(request, id):
    cancion=Cancion.objects.get(id=id)
    if request.method=="POST":
        form=formularioC(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            cancion.nombre=informacion["nombre"]
            cancion.duracion=informacion["duracion"]
            cancion.fechadesalida=informacion["fechadesalida"]
            cancion.save()
            canciones=Cancion.objects.all()
            return render (request, "leerCancion.html", {"mensaje": "CANCION EDITADA", "canciones":canciones})
    else:
        formulario=formularioC(initial={"nombre":cancion.nombre, "duracion":cancion.duracion, "fechadesalida":cancion.fechadesalida})
        return render(request, "editarCancion.html",{"form":formulario, "cancion":cancion})

#CRUD AUTOR
class AutorList(ListView):
    model= Autor
    template_name="leerAutor.html"

class AutorCreacion(CreateView):#PREGUNTAR POR TEMPLATES
    model = Autor
    success_url = reverse_lazy('autor_listar')
    template_name="autor_form.html"
    fields=['nombre', 'edad', 'fechadenacimiento']

class AutorUpdate(UpdateView):
    model= Autor
    success_url = reverse_lazy("autor_listar")
    template_name="autor_form.html"
    fields= ["nombre", "edad", "fechadenacimiento"]

class AutorDelete(DeleteView):
    model= Autor
    template_name="autor_confirm_delete.html"
    success_url = reverse_lazy("autor_listar")