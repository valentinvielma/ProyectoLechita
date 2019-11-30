from django.shortcuts import render, redirect
from .models import Leche
from .forms import LecheForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.

def index(request):
    return render(request, 'index.html')


def crud(request):
    return render(request, 'crud.html')


def list(request):
    leches = Leche.objects.all()
    return render(request, 'list.html', {'leches': leches})


def new(request):
    form = LecheForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'leche_form.html', {'form': form})


def update(request, id):
    leche = Leche.objects.get(id=id)
    form = LecheForm(request.POST or None, instance=leche)

    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'leche_form.html', {'form': form, 'leche': leche})


def delete(request, id):
    leche = Leche.objects.get(id=id)

    if request.method == 'POST':
        leche.delete()
        return redirect('list')

    return render(request, 'delete_leche_confirm.html', {'leche': leche})


def carrusel(request):
    return render(request, 'carrusel.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('index')
