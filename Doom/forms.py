from django import forms


class formularioC(forms.Form):
    nombre= forms.CharField(max_length=50)
    duracion=forms.IntegerField()
    fechadesalida=forms.DateField()

class formularioJ(forms.Form):
    nombre= forms.CharField(max_length=50)
    duracion=forms.IntegerField()
    fechadesalida=forms.DateField()

class formularioA(forms.Form):
    nombre= forms.CharField(max_length=50)
    edad=forms.IntegerField()
    fechadenacimiento=forms.DateField()
    