from django.urls import path
from .views import *


urlpatterns = [
    path("", enviarMensaje, name="mensaje")
]