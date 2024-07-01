from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import MandatoAporteForm
from .models import MandatoAporte
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('mandatos')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
        return  render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Contraseñas no coinciden'
                })

@login_required
def mandatos(request):
    usuario = request.user  # Obtén el usuario autenticado
    mandatos = MandatoAporte.objects.filter(user=request.user)
    return render(request, 'mandatos.html', {'mandatos': mandatos, 'usuario': usuario})

@login_required
def crear_mandato(request):
    if  request.method == 'GET':
        return render(request, 'crear_mandato.html',  {
            'form': MandatoAporteForm
        })
    else:
        try:
            form = MandatoAporteForm(request.POST)
            nuevo_aporte = form.save(commit=False)
            nuevo_aporte.user = request.user
            nuevo_aporte.save()
            return redirect('mandatos')
        except ValueError:
            return render(request, 'crear_mandato.html',  {
            'form': MandatoAporteForm,
            'error': 'Error al crear aporte'
        })

@login_required
def eliminar_mandato(request, mandato_id):
    if request.method == 'POST':
        mandato = get_object_or_404(MandatoAporte, pk=mandato_id, user=request.user)
        mandato.delete()
        return redirect('mandatos')

@login_required
def mandato_detalle(request, mandato_id):
    if request.method == 'GET':
        mandato = get_object_or_404(MandatoAporte, pk=mandato_id, user=request.user)
        form = MandatoAporteForm(instance=mandato)
        return render(request, 'mandato_detalle.html', {'mandato' : mandato, 'form': form})
    else:
        try:
            mandato = get_object_or_404(MandatoAporte, pk=mandato_id, user=request.user)
            form = MandatoAporteForm(request.POST, instance=mandato)
            form.save()
            return redirect('mandatos')
        except ValueError:
            return render(request, 'mandato_detalle.html', {'form': form, 'error': "Error al actualizar"})

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm(),
            'next': request.GET.get('next', '/mandatos')
        })
    else:
        user = authenticate(
            request, 
            username=request.POST['username'], 
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm(),
                'error': 'El usuario o contraseña es incorrecto'
            })
        else:
            login(request, user)
            return redirect('/mandatos')

