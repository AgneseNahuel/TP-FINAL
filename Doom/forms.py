from django import forms


class formularioC(forms.Form):
    nombre= forms.CharField(max_length=50)
    duracion=forms.IntegerField()
    fechadesalida=forms.DateField()