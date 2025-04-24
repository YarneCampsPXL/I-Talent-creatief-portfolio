from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def innovatie(request):
    return render(request, 'innovatie.html')

def seminaries(request):
    return render(request, 'seminaries.html')

def persoonlijke_ontwikkeling(request):
    return render(request, 'persoonlijke_ontwikkeling.html')

def internationalisering(request):
    return render(request, 'internationalisering.html')

def selectie(request):
    return render(request, 'selectie.html')

def eindrelfectie(request):
    return render(request, 'eindreflectie.html')
