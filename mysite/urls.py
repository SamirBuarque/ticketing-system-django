from django.contrib import admin
from django.urls import path
from .views import *
from django.urls import path, include
from userprofile.views import signup
from django.contrib.auth import views
from userprofile.views import *

urlpatterns = [
    path('', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('sobre/', sobre, name="sobre"),
    path('index/', index, name="index"),
    path('signup/', signup, name='signup'),
    path('logout/', logout.as_view(), name='logout'),
]