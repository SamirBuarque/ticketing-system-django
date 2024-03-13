from django.shortcuts import render

def home(request):
    return render(request, 'mysite/index.html', context={
        'name': 'Samir'
    })

def sobre(request):
    return render(request, 'mysite/sobre.html')

def login(request):
    return render(request, 'mysite/login.html')