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
    rol = ACLRole.objects.get(RoleName="Cliente")
    ACLUser(UserRole=rol, UserEmail=email, UserStatus=1).save()
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
    rol = ACLRole.objects.get(RoleName="Profesional")
    ACLUser(UserRole=rol, UserEmail=email, UserStatus=1).save()
    return render(request, 'index.html')


def login(request):
    if request.method=='POST':
        UserEmail_text = request.POST['email']
        User = ACLUser.objects.get(UserEmail=UserEmail_text)
        UserRole = User.UserRole
        UserRoleId = UserRole.getIdRole()
        Role = ACLRole.objects.get(IdRole=UserRoleId)
        RoleName = Role.RoleName
        if RoleName == 'Cliente':
            userclient=Client.objects.get(email=request.POST['email'], password=request.POST['password'])    
            request.session['email']=userclient.email
            return render(request, 'indexClient.html')
        elif Role.RoleName == 'Profesional':
            userprofessional=Professional.objects.get(email=request.POST['email'], password=request.POST['password']) 
            request.session['email']=userprofessional.email
            return render(request, 'indexProfessional.html')

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
    UserEmail = request.POST['UserEmail']
    UserStatus = request.POST['UserStatus']
    UserRole_text = request.POST['UserRole_text']
    UserRole = ACLRole.objects.get(RoleName=UserRole_text)
    ACLUser(UserRole=UserRole, UserEmail=UserEmail, UserStatus=UserStatus).save()
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
    if request.POST:
        SolicitudDescription = request.POST['SolicitudDescription']
        SolicitudClient = Client.objects.get(email=request.POST.get('SolicitudClient_email'))
        SolicitudProfession = Profession.objects.get(id=request.POST['SolicitudProfession_text'])
        SolicitudPrice = request.POST['SolicitudPrice']
        SolicitudDate = request.POST['SolicitudDate']
        SolicitudAddress = request.POST['SolicitudAddress']
        SolicitudImg = request.FILES.get('img')
        SolicitudStatus = "Pendiente"
        Requests(
            SolicitudProfession=SolicitudProfession, 
            SolicitudPrice=SolicitudPrice, 
            SolicitudDate=SolicitudDate, 
            SolicitudAddress=SolicitudAddress, 
            SolicitudImg=SolicitudImg, 
            SolicitudClient=SolicitudClient, 
            SolicitudDescription=SolicitudDescription, 
            SolicitudStatus=SolicitudStatus).save()
        return render(request, 'indexClient.html')


def registerSolicitud(request):
    return render(request, 'registerSolicitud.html')

def category(request):
    return render(request, 'categoria.html')

def requests(request):
    queryset = Profession.objects.all()
    context = {
		'objectList': queryset,
	}
    return render(request, 'solicitud.html', context)

def cambProfessional(request):
    if request.POST:
        
        abc=Professional.objects.get(id=request.POST['id'])
        abc.names=request.POST['names']
        abc.surnames=request.FILES.get('surnames')
        abc.email=request.POST['email']
        abc.telephone=request.POST['telephone']
        abc.dni=request.POST['dni']
        abc.date=request.POST['date']
        ###############
        var=Profession.POST['profession']
        abc.profession=Profession.object.get(id=var.name)
        ################
        abc.save()
        queryset = Requests.objects.all()
        context = {
            'objectList': queryset,
        }
        return render(request,'solicitud_edit.html',context )

def editProfessional(request):
    if request.POST:
        abc=Professional.objects.get(email=request.POST['id'])
        abc.names = request.POST['names']
        abc.surnames = request.POST['surnames']
        abc.telephone = request.POST['telephone']
        abc.dni = request.POST['dni']
        abc.date = request.POST['date']
        abc.profession = Profession.objects.get(id=request.POST['profession'])
        abc.img = request.FILES.get('img')
        abc.description = request.POST['desc']
        abc.save()
    #return render(request,'solicitud_edit.html',context )
    return render(request, 'index.html')

def movEditProfessional(request):
    query1=Professional.objects.get(email=request.POST['email'])
    prof=Profession.objects.all()
    context = {
        'objectList': query1,
        'objectList1': prof,
    }
    
    return render(request,'perfilprofesional_edit.html',context )

def deleteProfessional(request):
    var=Requests.objects.get(id=request.POST['id'])
    var.delete()    
    queryset = Requests.objects.all()
    context = {
        'objectList': queryset,
    }
    return render(request, '''indexProfessional''', context)
    #############################


def bandejaMSG(request):
    return render(request, 'bandejamsg.html')

def indexClient(request):
    return render(request, 'indexClient.html')

def indexProfessional(request):
    queryset = Requests.objects.all()
    q2 = Profession.objects.all()
    context = {
        'objectList': queryset,
        'objectList2': q2,
    }
    return render(request, 'indexProfessional.html', context)

def aceptarSolicitud(request):
    Solicitud = Requests.objects.get(id=request.POST.get('id'))
    Solicitud.SolicitudStatus = "Aceptada"
    Solicitud.save()
    #.delete()
    return render(request, 'indexProfessional.html')


# Requests-Solicitud


def managingRequests(request):
    queryset = Requests.objects.all()
    context = {
		'objectList': queryset,
	}
    return render(request, 'gestionarsolicitudes.html', context)
def listRequests(request):
    queryset = Requests.objects.all()
    context = {
		'objectList': queryset,
	}
    return render(request, 'listaSolicitudes.html', context)
# funcion myID
def detailsRequests(request, myID):
    queryset = get_object_or_404(Requests, id = myID)
    context = {
        'objectList': queryset,
    }
    return render(request, 'detalleSolicitud.html', context)


def movEditRequests(request):
    abc=Requests.objects.get(id=request.POST['id'])
    prof=Profession.objects.all()
    context = {
        'objectList': abc,
        'objectList1': prof,
    }
    
    return render(request,'solicitud_edit.html',context )

def editRequests(request):
     
    if request.POST:
        
        abc=Requests.objects.get(id=request.POST['SolicitudId'])
        #abc.SolicitudId=Requests.objects.get(id=request.POST['SolicitudId'])
        abc.SolicitudDescription=request.POST['SolicitudDescription']
        abc.SolicitudImg=request.FILES.get('SolicitudImg')
        abc.SolicitudDate=request.POST['SolicitudDate']
        abc.SolicitudAddress=request.POST['SolicitudAddress']
        abc.SolicitudPrice=request.POST['SolicitudPrice']
        ###############
        print(request.POST['SolicitudProfession'])
        var=Profession.objects.get(id=request.POST['SolicitudProfession'])
        #print(var)
        abc.SolicitudProfession=var
        ################
        abc.save()
        queryset = Requests.objects.all()
        context = {
            'objectList': queryset,
        }
        return render(request,'solicitud_edit.html',context )

def deleteRequests(request):
    var=Requests.objects.get(id=request.POST['id'])
    var.delete()
    
    queryset = Requests.objects.all()
    context = {
        'objectList': queryset,
    }
    """ 
    queryset.delete() """
    return render(request, 'gestionarsolicitudes.html', context)
