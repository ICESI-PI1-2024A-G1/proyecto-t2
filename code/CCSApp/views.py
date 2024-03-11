from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def gestion(request):
    return render(request, 'gestion.html')

def empezar_pogra(request):
    return render(request, 'empezar_progra.html')

def log_in(request):
    return render(request, 'log_in.html')

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')
