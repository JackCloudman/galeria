from django.shortcuts import render
from .models import Foto
def home(request):
    fotos = Foto.objects.order_by('fecha')
    return render(request, 'index.html', {'fotos':fotos})

# Create your views here.
