from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("bio/", biografia, name="biografia"),
    path("doom/", Doom, name="doom"),
]