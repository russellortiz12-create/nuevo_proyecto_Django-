from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })

# otra ruta
def about(request):
    return render(request, 'mainapp/about.html', {
        'title': 'Sobre Nosotros'
    })

def register_page(request):
    # Corrección: is_authenticated es un atributo (sin paréntesis)
    if request.user.is_authenticated:
        return redirect('inicio')
        
    register_form = RegisterForm()
    
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Se ha Registrado Correctamente!!!')
            return redirect('inicio')
            
    return render(request, 'users/register.html', {
        'title': 'Registro',
        'register_form': register_form
    })
    
def login_page(request):
    # Corrección: is_authenticated sin paréntesis
    if request.user.is_authenticated:
        return redirect('inicio')
         
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.warning(request, 'No ha podido iniciar sesión!!!')

    return render(request, 'users/login.html', {
        'title': 'Identifícate'
    })

def logout_user(request):
    logout(request)
    return redirect('login')