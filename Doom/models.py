from django.db import models

# Create your models here.
class Cancion(models.Model):

    nombre= models.CharField(max_length=50)
    duracion=models.IntegerField()
    fechadesalida=models.DateField(max_length=50)

    def __str__(self) -> str:
        return self.nombre+" "+self.duracion+" "+self.fechadesalida

class clientes(models.Model):

    nombre= models.CharField(max_length=50)
    duracion=models.IntegerField()
    fechadesalida=models.DateField(max_length=50)

    def __str__(self) -> str:
        return self.nombre+" "+self.duracion+" "+self.fechadesalida

class Autor(models.Model):

    nombre= models.CharField(max_length=50)
    edad=models.IntegerField()
    fechadenacimiento=models.DateField(max_length=50)

    def __str__(self) -> str:
        return self.nombre+" "+self.edad+" "+self.fechadenacimiento