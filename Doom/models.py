from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cancion(models.Model):

    nombre= models.CharField(max_length=50)
    duracion=models.IntegerField()
    fechadesalida=models.DateField(max_length=50)

    def __str__(self) -> str:
        return self.nombre+" "+str(self.duracion)+" "+str(self.fechadesalida)

class Juego(models.Model):

    nombre= models.CharField(max_length=50)
    duracion=models.IntegerField()
    fechadesalida=models.DateField(max_length=50)

    def __str__(self) -> str:
        return self.nombre+" "+str(self.duracion)+" "+str(self.fechadesalida)

class Autor(models.Model):

    nombre= models.CharField(max_length=50)
    edad=models.IntegerField()
    fechadenacimiento=models.DateField(max_length=50)

    def __str__(self) -> str:
        return self.nombre+" "+str(self.edad)+" "+str(self.fechadenacimiento)

class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatares")
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"