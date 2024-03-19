from django.contrib import admin
from django.urls import path
from .views import *
from django.urls import path, include
from userprofile.views import signup
#from django.contrib.auth import views
from userprofile.views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', custom_login, name="custom_login"),
    path('sobre/', sobre, name="sobre"),
    path('signup/', signup, name='signup'),
    path('logout/', custom_logout, name='logout'),
]