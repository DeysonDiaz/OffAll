from django.contrib import admin
from .models import Client, Profession, Professional
# Register your models here.
admin.site.register(Client)
admin.site.register(Profession)
admin.site.register(Professional)