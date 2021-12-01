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
]