#importante cambiar con cada vista  (views)
#añadir el llamado en url de offall.url
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home')
]
