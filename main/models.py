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