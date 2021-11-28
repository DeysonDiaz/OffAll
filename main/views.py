from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registerclient(request):
    return render(request, 'registerclient.html')

def registerprofessional(request):
    return render(request, 'registerprofessional.html')