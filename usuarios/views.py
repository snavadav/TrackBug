from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, TicketForm, PerfilForm
from django.http import HttpResponse
from .models import Ticket
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('dashboard')  # cambia 'home' según tu URL principal
        else:
            return render(request, 'usuarios/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'usuarios/login.html')

#Vista para registrar usuarios
def registro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def dashboard(request):
    tickets = Ticket.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'usuarios/dashboard.html', {'tickets': tickets})

@login_required
def nuevo_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.usuario = request.user
            ticket.save()
            return redirect('dashboard')
    else:
        form = TicketForm()
    return render(request, 'usuarios/nuevo_ticket.html', {'form': form})

def ver_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, usuario=request.user)
    return render(request, 'usuarios/ver_ticket.html', {'ticket': ticket})

@login_required
def perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=request.user)

    return render(request, 'usuarios/perfil.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')