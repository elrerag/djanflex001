from django.shortcuts import render
from django.views import generic
from .models import Persona

# Create your views here.

class PersonaListView(generic.ListView):
    """encargado lista las ofertas"""
    model = Persona