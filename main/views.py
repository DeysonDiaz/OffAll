from django.core.checks import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Profession, Professional

def index(request):
    return render(request, 'index.html')

def createclient(request):
    names = request.POST['nombre']
    surnames = request.POST['apellido']
    email = request.POST['email']
    password = request.POST['password']
    telephone = request.POST['cell']
    dni = request.POST['dni']
    date = request.POST['fechan']
    Client(names=names, surnames=surnames, email=email, password=password, telephone=telephone, dni=dni, date=date).save()
    return render(request, 'index.html')

def createprofessional(request):
    names = request.POST['nombre']
    surnames = request.POST['apellido']
    email = request.POST['email']
    password = request.POST['password']
    telephone = request.POST['cell']
    dni = request.POST['dni']
    date = request.POST['fechan']
    profession = Profession.objects.get(id=request.POST['cat'])
    img = request.POST['img']
    description = request.POST['desc']
    Professional(names=names, surnames=surnames, email=email, password=password, telephone=telephone, dni=dni, date=date, profession=profession, img=img, description=description).save()
    return render(request, 'index.html')


def login(request):
    if request.method=='POST':
        print("Este es el request", request.POST['rol'])
        if request.POST['rol'] == 'cliente':
            print('entro a cliente')
            userclient=Client.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['email']=userclient.email
        if request.POST['rol'] == 'profesional':
            userprofessional=Professional.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['email']=userprofessional.email
    return render(request, 'index.html')

def logout(request):
    del request.session['email']
    return render(request, 'index.html')

def registerprofessional(request):
    queryset = Profession.objects.all()
    context = {
		'objectList': queryset,
	}
    return render(request, 'registerprofessional.html', context)

def registerclient(request):
    return render(request, 'registerclient.html')
