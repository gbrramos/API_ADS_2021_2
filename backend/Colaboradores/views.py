from django.shortcuts import render
from django.http import HttpResponse
from models import Colaboradores

# Create your views here.

def lista(request):
    for p in Colaboradores.objects.raw('Select * from colaboradores'):
        print(p)