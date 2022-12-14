from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class chat(forms.Form):
    emisor= forms.CharField()
    receptor=forms.CharField()
    cuerpo=forms.CharField()
    leido=forms.BooleanField()
    