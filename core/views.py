from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout, get_user_model
from .models import paciente

User = get_user_model()


if not User.objects.filter(username="Admin").exists():  
    admin_user = User.objects.create_user(username="Admin", password="123456", email="Admin@gmail.com")
    admin_user.save()


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  
            print("Usuário autenticado!")
            return redirect('index')
        else:
            print("Usuário ou senha inválidos.")
            return render(request, "login.html", {"error": "Usuário ou senha inválidos."})

    return render(request, "login.html")


def index(request):
    usuario = request.user 
    return render(request, "index.html", {"usuario": usuario})


def listar_paciente(request):
    paciente = paciente.objects.all()
    return render(request, 'listar_paciente.html', {'paciente': paciente})


def adicionar_paciente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        paciente.objects.create(nome=nome)
        return redirect('listar_paciente')
    return render(request, 'adicionar_paciente.html')


def editar_paciente(request, id):
    paciente = get_object_or_404(paciente, id=id)
    if request.method == 'POST':
        paciente.nome = request.POST.get('nome')
        paciente.save()
        return redirect('listar_paciente')
    return render(request, 'editar_paciente.html', {'paciente': paciente})


def deletar_paciente(request, id):
    paciente = get_object_or_404(paciente, id=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('listar_paciente')
    return render(request, 'deletar_paciente.html', {'paciente': paciente})


def monitorar_paciente(request):
    pacientes = pacientes.objects.all()
    return render(request, 'monitorar_paciente.html', {'paciente': paciente})
