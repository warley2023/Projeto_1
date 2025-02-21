from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente


#user = User.objects.create_user(username="Admin", password="123456", email="Admin@email.com")
#user.save()


def minha_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            print("Usuário autenticado!")
            return redirect("home")
        else:
            print("Usuário ou senha inválidos.")
            return render(request, "login.html", {"error": "Usuário ou senha inválidos."})

    return render(request, "login.html")

def index(request):

    return render( request, "index.html") 




def listar_paciente(request):
    pacientes = Paciente.objects.all()
    return render(request, 'listar_paciente.html', {'pacientes': pacientes})

def adicionar_paciente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        Paciente.objects.create(nome=nome)
        return redirect('listar_pacientes')
    return render(request, 'adicionar_paciente.html')

def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        paciente.nome = request.POST.get('nome')
        paciente.save()
        return redirect('listar_pacientes')
    return render(request, 'editar_paciente.html', {'paciente': paciente})

def deletar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('listar_pacientes')
    return render(request, 'deletar_paciente.html', {'paciente': paciente})


def monitorar_paciente(request):
    pacientes = Paciente.objects.all() 
    return render(request, 'monitorar_paciente.html', {'pacientes': pacientes})

