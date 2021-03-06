from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("registerclient", views.registerclient, name = "registerclient"),
	path("registerprofessional", views.registerprofessional, name = "registerprofessional"),
    path("createclient", views.createclient, name = "createclient"),
    path("createprofessional", views.createprofessional, name = "createprofessional"),
    path("login", views.login, name = "login"),
    path("logout", views.logout, name = "logout"),
    path("registerACLRole", views.registerACLRole, name = "registerACLRole"),
    path("createACLRole", views.createACLRole, name = "createACLRole"),
	path("registerACLResource", views.registerACLResource, name = "registerACLResource"),
    path("createACLResource", views.createACLResource, name = "createACLResource"),
    path("registerACLUser", views.registerACLUser, name = "registerACLUser"),
    path("createACLUser", views.createACLUser, name = "createACLUser"),
    path("registerACLAccess", views.registerACLAccess, name = "registerACLAccess"),
    path("createACLAccess", views.createACLAccess, name = "createACLAccess"),
    path("registerSolicitud", views.registerSolicitud, name = "registerSolicitud"),
    path("createSolicitud", views.createSolicitud, name = "createSolicitud"),
    path("category", views.category, name= "category"),
    path("managingRequests", views.managingRequests, name= "managingRequests"),
    path("requests", views.requests, name= "requests"),
    path("listRequests", views.listRequests, name= "listRequests"),
    #url con el id
    path("detailsRequests/<int:myID>", views.detailsRequests, name= "detailsRequests"),
    ##
    path("deleteRequests", views.deleteRequests, name = "deleteRequests"),
    path("movEditRequests", views.movEditRequests, name= "movEditRequests"),
    ##
    path("editProfessional", views.editProfessional, name= "editProfessional"),
    path("movEditProfessional", views.movEditProfessional, name= "movEditProfessional"),
    path("bandejaMSG", views.bandejaMSG, name= "bandejaMSG"),
    path("editRequests", views.editRequests, name= "editRequests"),
    
    path('indexClient', views.indexClient, name='indexClient'),
    path('indexProfessional', views.indexProfessional, name='indexProfessional'),
    path('aceptarSolicitud', views.aceptarSolicitud, name='aceptarSolicitud')
       
]