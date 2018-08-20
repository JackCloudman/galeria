from django.shortcuts import render
from .models import Foto
def home(request):
    fotos = Foto.objects.order_by('-fecha')[:5]
    return render(request, 'index.html', {'fotos':fotos})
def galeria(request):
    fotos = Foto.objects.order_by('-fecha')
    return render(request, 'galeria.html', {'fotos':fotos})

# Create your views here.
