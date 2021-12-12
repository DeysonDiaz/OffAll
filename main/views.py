from django.core.checks import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import *

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
    profession = request.POST['cat']
    img = request.POST['img']
    description = request.POST['desc']
    Professional(names=names, surnames=surnames, email=email, password=password, telephone=telephone, dni=dni, date=date, profession=profession, img=img, description=description).save()
    return render(request, 'index.html')

def login(request):
    if request.method=='POST':
        var1=userclient=Client.objects.get(email=request.POST['email'], password=request.POST['password'])
        #userprofessional=Professional.objects.get(email=request.POST['email'], password=request.POST['password'])
        '''if userclient:
            request.session['email']==userclient.email
        else:
            request.session['email']==userprofessional.email'''
        request.session['email']=userclient.email
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

def createACLRole(request):
    RoleName = request.POST['RoleName']
    RoleStatus = request.POST['RoleStatus']
    ACLRole(RoleName=RoleName, RoleStatus=RoleStatus).save()
    return render(request, 'index.html')

def registerACLRole(request):
    return render(request, 'registerACLRole.html')

def createACLResource(request):
    ResourceName = request.POST['ResourceName']
    ResourceStatus = request.POST['ResourceStatus']
    ACLResource(ResourceName=ResourceName, ResourceStatus=ResourceStatus).save()
    return render(request, 'index.html')

def registerACLResource(request):
    return render(request, 'registerACLResource.html')

def createACLUser(request):
    UserName = request.POST['UserName']
    UserStatus = request.POST['UserStatus']
    UserRole_text = request.POST['UserRole_text']
    UserRole = ACLRole.objects.get(RoleName=UserRole_text)
    ACLUser(UserRole=UserRole, UserName=UserName, UserStatus=UserStatus).save()
    return render(request, 'index.html')

def registerACLUser(request):
    return render(request, 'registerACLUser.html')

def createACLAccess(request):
    AccessName = request.POST['AccessName']
    AccessStatus = request.POST['AccessStatus']
    AccessRole_text = request.POST['AccessRole_text']
    AccessRole = ACLRole.objects.get(RoleName=AccessRole_text)
    AccessResource_text = request.POST['AccessResource_text']
    AccessResource = ACLResource.objects.get(ResourceName=AccessResource_text)
    ACLAccess(AccessRole=AccessRole, AccessResource=AccessResource, AccessName=AccessName, AccessStatus=AccessStatus).save()
    return render(request, 'index.html')

def registerACLAccess(request):
    return render(request, 'registerACLAccess.html')

def createSolicitud(request):
    SolicitudDescription = request.POST['SolicitudDescription']
    SolicitudStatus = request.POST['SolicitudStatus']
    SolicitudClient_text = request.POST['SolicitudClient_text']
    SolicitudClient = Client.objects.get(names=SolicitudClient_text)
    SolicitudProfessional_text = request.POST['SolicitudProfessional_text']
    SolicitudProfessional = Professional.objects.get(names=SolicitudProfessional_text)
    Solicitud(SolicitudProfessional=SolicitudProfessional, SolicitudClient=SolicitudClient, SolicitudDescription=SolicitudDescription, SolicitudStatus=SolicitudStatus).save()
    return render(request, 'index.html')

def registerSolicitud(request):
    return render(request, 'registerSolicitud.html')

def category(request):
    return render(request, 'categoria.html')

def managingRequests(request):
    return render(request, 'gestionarsolicitudes.html')

def requests(request):
    return render(request, 'solicitud.html')

def listRequests(request):
    return render(request, 'listaSolicitudes.html')

def detailsRequests(request):
    return render(request, 'detalleSolicitud.html')

def editProfessional(request):
    return render(request, 'perfilprofesional_edit.html')

def bandejaMSG(request):
    return render(request, 'bandejamsg.html')

def editRequests(request):
    return render(request, 'solicitud_edit.html')



