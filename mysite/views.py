from django.shortcuts import render
from http import HTTPMethod

def index(request):
    return render(request, 'mysite/index.html')

def sobre(request):
    return render(request, 'mysite/sobre.html')

def login(request):
    return render(request, 'mysite/login.html')