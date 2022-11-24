from django.urls import path
from Doom.views import *

urlpatterns = [
    path("", inicio, name=inicio),
]