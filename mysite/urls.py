from django.contrib import admin
from django.urls import path
from .views import *
from django.urls import path, include
#from django.contrib.auth import views
from userprofile.views import *

urlpatterns = [
    path('', index, name='index'),
]