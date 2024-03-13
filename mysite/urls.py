from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='index'),
    path('sobre/', views.sobre, name="sobre"),
    path('login/', views.login, name="login"),
]