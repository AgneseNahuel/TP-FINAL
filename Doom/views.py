from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def inicio(request):
    return render(request, "templates\inicio.html")