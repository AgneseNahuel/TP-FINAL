from django.shortcuts import render
from .models import *
from Doom.models import *
from .forms import *
from Doom.forms import *
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin #vistas basadas en clases
from django.contrib.auth.decorators import login_required #vistas basadas en funciones

def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/avatarpordefecto.png"
    return imagen

@login_required
def enviarMensaje(request):
    if request.method=="POST":
        form=chat(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            emisor=informacion["emisor"]
            #receptor=informacion["receptor"]
            leido=informacion["leido"]
            cuerpo=informacion["cuerpo"]
            
            mens=chat(emisor=emisor, leido=leido, cuerpo=cuerpo)
            mens.save()
            return render (request, "chat.html", {"mensaje":"se creo bien", "imagen":obtenerAvatar(request)})
        else:
            formulario=chat
            return render(request, "chat.html", {"formulario":formulario}, {"mensaje":"error", "imagen":obtenerAvatar(request)})
    else:
        formulario=chat
    return render(request, "chat.html", {"formulario":formulario, "imagen":obtenerAvatar(request)})


@login_required
def leerMensajes(request):
    #TRAER MENSAJES
    pass
