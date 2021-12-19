from django.db import models

# Create your models here.
class Client(models.Model):

    names = models.CharField(max_length = 200)
    surnames = models.CharField(max_length = 200)
    email = models.EmailField(max_length= 200)
    password = models.CharField(max_length = 200)
    telephone = models.IntegerField()
    dni = models.IntegerField()
    date = models.DateField()
	
    def __str__(self):
        return self.names

class Profession(models.Model):

    name = models.CharField(max_length = 200)
    description = models.TextField()
	
    def __str__(self):
        return self.name


class Professional(models.Model):

    names = models.CharField(max_length = 200)
    surnames = models.CharField(max_length = 200)
    email = models.EmailField(max_length= 200)
    password = models.CharField(max_length = 200)
    telephone = models.IntegerField()
    dni = models.IntegerField()
    date = models.DateField()
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    img = models.ImageField(upload_to = 'pics')
    description = models.TextField()
	
    def __str__(self):
        return self.names
    
class ACLRole(models.Model):
    IdRole = models.AutoField(primary_key=True)
    RoleName = models.CharField(max_length=200)
    RoleStatus = models.IntegerField()
    def getIdRole(self):
        return self.IdRole
    
class ACLResource(models.Model):
    IdResource = models.AutoField(primary_key=True)
    ResourceName = models.CharField(max_length=200)
    ResourceStatus = models.IntegerField()

class ACLUser(models.Model):
    IdUser = models.AutoField(primary_key=True)
    UserEmail = models.CharField(max_length=40)
    UserStatus = models.IntegerField()
    UserRole = models.ForeignKey(ACLRole, null=False, blank=False, on_delete=models.CASCADE)

class ACLAccess(models.Model):
    IdAccess = models.AutoField(primary_key=True)
    AccessName = models.CharField(max_length=60)
    AccessStatus = models.IntegerField()
    AccessRole = models.ForeignKey(ACLRole, null=False, blank=False, on_delete=models.CASCADE)
    AccessResource = models.ForeignKey(ACLResource, null=False, blank=False, on_delete=models.CASCADE)

class Requests(models.Model):
    SolicitudDescription = models.CharField(max_length=5000)
    SolicitudImg = models.ImageField(upload_to = 'pics')
    SolicitudDate = models.DateField()
    SolicitudProfession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    SolicitudAddress = models.CharField(max_length=100)
    SolicitudPrice = models.FloatField()
    SolicitudClient = models.ForeignKey(Client, null=False, blank=False, on_delete=models.CASCADE)
    SolicitudStatus = models.CharField(max_length=100)

#funcion de url
    def get_mos_url(self):
        return "detailsRequests/"+str(self.id)