from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'mysite/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)

            return redirect('mysite/index.html')
    else:    
        form = UserCreationForm()
    return render(request, "userprofile/signup.html", {'form': form})

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                error_message = 'Erro ao efetuar login. Credenciais inválidas'
        else:
            error_message = 'Por favor preencha todos os campos'

        return render(request, "userprofile/login.html", {'error_message': error_message})
              
    else:
        return render(request, "userprofile/login.html")

def custom_logout(request):
    logout(request)
    return redirect("custom_logout")
    
    

