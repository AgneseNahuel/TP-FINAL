from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("formularioAutor/", formularioAutor, name="formularioAutor"),
    path("formularioJuego/", formularioJuego, name="formularioJuego"),
    path("formularioCancion/", formularioCancion, name="formularioCancion"),
    path("buscarc/", busquedac, name="buscarc"),
    path("buscar/", buscarc, name="buscar"),
    path("leercanciones/", leerCanciones, name="leercanciones"),#LISTADO
    path("eliminarCancion/<id>", eliminarCanciones, name="eliminarCancion"),
    path("editarCancion/<id>", editarCancion, name="editarCancion"),

    path("autor/list/", AutorList.as_view(), name="autor_listar"),#LISTADO AUTOR CON CLASES
    path("autor/nuevo/", AutorCreacion.as_view(), name="autor_crear"),
    path("autor/editar/<pk>", AutorUpdate.as_view(), name="autor_editar"),
    path("autor/borrar/<pk>", AutorDelete.as_view(), name="autor_borrar"),
]