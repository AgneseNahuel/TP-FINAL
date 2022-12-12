from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Al crear una nueva clase, no olvidar makemigrations y migrate...
#Si se agregan campos meter un default o un null
#La fecha por default es año/mes/dia
class formularioC(forms.Form):
    nombre= forms.CharField(max_length=50)
    duracion=forms.IntegerField()
    fechadesalida=forms.DateField()#default="2021-01-01" / null=True
    #fechadesalida= forms.DateField(input_formats=["%d/%m/%Y"])... esta es otra manera de organizar

class formularioJ(forms.Form):
    nombre= forms.CharField(max_length=50)
    duracion=forms.IntegerField()
    fechadesalida=forms.DateField()#Para cambiar la manera que se introduce la fecha se usa (format= "xx-xx-xx")

class formularioA(forms.Form):
    nombre= forms.CharField(max_length=50)
    edad=forms.IntegerField()
    fechadenacimiento=forms.DateField()

class RegistroUsuarioForm(UserCreationForm):
    password1= forms.CharField(label="Ingrese contraseña: ", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita contraseña: ", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields = ["username", "password1", "password2"]
        help_text = {k:"" for k in fields }#para eliminar los avisos de los campos

class UserEditForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Modificar Nombre")
    last_name=forms.CharField(label="Modificar Apellido")

    class Meta:
        model= User
        fields= ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="imagen")
