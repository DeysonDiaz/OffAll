from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Client)
admin.site.register(Profession)
admin.site.register(Professional)
admin.site.register(ACLRole)
admin.site.register(ACLResource)
admin.site.register(ACLUser)
admin.site.register(ACLAccess)
admin.site.register(Solicitud)

