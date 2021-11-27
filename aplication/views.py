#importante cambiar con cada vista  (views)


from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello World")

