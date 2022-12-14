from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Doom.models import *
from .forms import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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
# Create your views here.
def inicio(request):
    lista=Avatar.objects.filter(user=request.user)
    return render (request, "inicio.html", {"imagen":obtenerAvatar(request)})

@login_required
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
            return render (request, "inicio.html", {"mensaje":"se creo bien", "imagen":obtenerAvatar(request)})
        else:
            formulario=formularioA
            return render(request, "formularioAutor.html", {"form":formulario}, {"mensaje":"error", "imagen":obtenerAvatar(request)})
    else:
        formulario=formularioA
    return render(request, "formularioAutor.html", {"form":formulario, "imagen":obtenerAvatar(request)})

@login_required
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
            return render (request, "inicio.html", {"mensaje":"se creo bien", "imagen":obtenerAvatar(request)})
    else:
        formulario=formularioJ()

    return render(request, "formularioJuego.html", {"form":formulario, "imagen":obtenerAvatar(request)})

@login_required
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
    return render(request, "formularioCancion.html", {"form":formulario, "imagen":obtenerAvatar(request)})

@login_required
#esta es la vista para buscar
def busquedac(request):
    return render(request, "busquedac.html")
@login_required
def buscarc(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        nombrec=Cancion.objects.filter(nombre__icontains=nombre)#__icontains, no tiene que ser exacto
        return render(request, "resultadocancion.html", {"nombrec":nombrec, "imagen":obtenerAvatar(request)})
    else:
        return render(request, "busquedac.html", {"mensaje":"NO VALIDO", "imagen":obtenerAvatar(request)})

#CRUD CANCION!!
@login_required
def leerCanciones(request):
    canciones=Cancion.objects.all()
    return render(request, "LeerCancion.html", {"canciones": canciones})

@login_required
def eliminarCanciones(request, id):
    cancion=Cancion.objects.get(id=id)
    cancion.delete()
    canciones=Cancion.objects.all()
    return render(request, "LeerCancion.html", {"mensaje":"CANCION ELIMINADA", "canciones":canciones})

@login_required
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
            return render (request, "leerCancion.html", {"mensaje": "CANCION EDITADA", "canciones":canciones, "imagen":obtenerAvatar(request)})
    else:
        formulario=formularioC(initial={"nombre":cancion.nombre, "duracion":cancion.duracion, "fechadesalida":cancion.fechadesalida, "imagen":obtenerAvatar(request)})
        return render(request, "editarCancion.html",{"form":formulario, "cancion":cancion})


#CRUD AUTOR
class AutorList(LoginRequiredMixin, ListView):
    model= Autor
    template_name="leerAutor.html"

class AutorCreacion(LoginRequiredMixin, CreateView):#PREGUNTAR POR TEMPLATES
    model = Autor
    success_url = reverse_lazy('autor_listar')
    template_name="autor_form.html"
    fields=['nombre', 'edad', 'fechadenacimiento']

class AutorUpdate(LoginRequiredMixin, UpdateView):
    model= Autor
    success_url = reverse_lazy("autor_listar")
    template_name="autor_form.html"
    fields= ["nombre", "edad", "fechadenacimiento"]

class AutorDelete(LoginRequiredMixin, DeleteView):
    model= Autor
    template_name="autor_confirm_delete.html"
    success_url = reverse_lazy("autor_listar")


#--------------LOGIN------------------------#

def login_request(request):
    if request.method == "POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "login.html", {"mensaje":"Incorrecto", "form":form})
        else:
            return render(request, "login.html", {"mensaje":"Incorrecto", "form":form})
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form":form})

#---------------REGISTRO---------------------#

def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render(request, "inicio.html", {"mensaje":f"usuario {username} creado"})
        else:
            return render(request, "register.html", {"form":form, "mensaje":"error"})
    else:
        form=RegistroUsuarioForm()
    return render(request, "register.html", {"form":form})

@login_required
def editarPerfil(request):
    usuario= request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "inicio.html", {"mensaje":"Perfil editado correctamente"})
        else:
            return render(request, "editarUsuario.html", {"mensaje":"Perfil editado correctamente", "form":form, "nombreusuario":usuario.username})     
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "editarUsuario.html", {"form":form, "nombreusuario":usuario.username, "imagen":obtenerAvatar(request)})

@login_required
def AgregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)#TRAE ARCHIVOS CON EL "FILES"
        if form.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)!=0:
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatar.save()
            return render(request, "inicio.html", {"mensaje":"Avatar agregado correctamente", "imagen":obtenerAvatar(request)})
        else:
            return render(request, "AgregarAvatar.html", {"formulario":form, "usuario":request.user, "imagen":obtenerAvatar(request)})
    else:
        form=AvatarForm()
        return render(request, "AgregarAvatar.html", {"formulario":form, "usuario":request.user, "imagen":obtenerAvatar(request)})

@login_required
def aboutMe(request):
    return render (request, "AcercaDeMi.html", {"imagen":obtenerAvatar(request)})

