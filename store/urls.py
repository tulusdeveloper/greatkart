from django.contrib import admin
from django.urls import path

from greatkart import settings
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   
    path('', views.store, name='store'),
] 
