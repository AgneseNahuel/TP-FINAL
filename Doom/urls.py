from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("formularioAutor/", formularioAutor, name="formularioAutor"),
    path("formularioJuego/", formularioJuego, name="formularioJuego"),
    path("formularioCancion/", formularioCancion, name="formularioCancion"),
]