from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
<<<<<<< Updated upstream
=======
def malla_curricular(request):
    return render(request, 'np_malla_curricular.html')

def nuevo_programa(request):
    return render(request, 'nuevo_programa.html')

def gestion(request):
    return render(request, 'gestion.html')

def empezar_pogra(request):
    return render(request, 'empezar_progra.html')

def log_in(request):
    return render(request, 'log_in.html')
>>>>>>> Stashed changes

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')
