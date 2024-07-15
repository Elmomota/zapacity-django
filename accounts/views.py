from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError

def signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html', {
            'form': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('shop:product_list')
            except IntegrityError:
                return render(request, 'accounts/signup.html', {
                    'form': UserCreationForm(),
                    'error': 'El usuario ya existe'
                })
        else:
            return render(request, 'accounts/signup.html', {
                'form': UserCreationForm(),
                'error': 'Las contraseñas no coinciden'
            })

def signin(request):
    if request.method == 'GET':
        return render(request, 'accounts/signin.html', {
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'accounts/signin.html', {
                'form': AuthenticationForm(),
                'error': 'El nombre de usuario o la contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('shop:product_list')

def signout(request):
    logout(request)
    return redirect('shop:product_list')
