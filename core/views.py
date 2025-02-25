from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
#from .models import Paciente
from core.models import Paciente
from decimal import Decimal
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from .forms import CadastroForm

@login_required
def home(request):
    
    pacientes_espera = Paciente.objects.filter(status='aguardando')
    pacientes_chamados = Paciente.objects.filter(status='atendimento')
    pacientes_evadidos = Paciente.objects.filter(destino='evadiu').order_by('data_hora_entrada') # Query para pacientes evadidos
        
    return render(request, 'home.html', {
        'pacientes_espera': pacientes_espera,
        'pacientes_chamados': pacientes_chamados,
        'pacientes_evadidos': pacientes_evadidos,  # Adicione esta linha   
        }
    )
    return render(request, 'home.html', {
        'pacientes_chamados': pacientes_chamados,
        }
    )
    
@login_required
def adicionar_paciente(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        temperatura = request.POST['temperatura']
        pressao_sistolica = request.POST.get('pressao_sistolica')
        pressao_diastolica = request.POST.get('pressao_diastolica')
        urgencia = request.POST['urgencia']

        Paciente.objects.create(
            nome=nome,
            temperatura=temperatura,
            pressao_sistolica=pressao_sistolica,
            pressao_diastolica=pressao_diastolica,
            urgencia=urgencia,
            status='aguardando'  # Define o status como "aguardando"
        )
        return redirect('home')  # Redireciona para a página inicial
    return render(request, 'adicionar_paciente.html')

@login_required
def chamar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    return render(request, 'chamar_paciente.html', {'paciente': paciente})

@login_required
def deletar_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('home')
    return render(request, 'deletar_paciente.html', {'paciente': paciente})

@login_required
def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    if request.method == 'POST':
        paciente.nome = request.POST.get('nome')
        # Adicione aqui a lógica para os outros campos
        paciente.save()
        return redirect('home')
    return render(request, 'editar_paciente.html', {'paciente': paciente})

@login_required
def monitorar_paciente(request):
    pacientes = Paciente.objects.all()
    return render(request, 'monitorar_paciente.html', {'pacientes': pacientes})
    
@login_required
def paciente_evadiu(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    paciente.status = 'evadiu'
    paciente.destino = 'Evadiu'
    paciente.save()
    return redirect('home')
    
@login_required
def paciente_alta(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    paciente.status = 'alta'
    paciente.save()
    return redirect('home')
    
@login_required
def paciente_atendimento(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    if request.method == 'POST':
        paciente.status = 'atendimento'
        paciente.destino = request.POST.get('destino')  # Obtém o destino do formulário POST
        paciente.save()
        return redirect('home')
    return redirect('chamar_paciente', paciente_id=paciente_id) #Redireciona caso não seja POST
    
def recepcao(request):
    pacientes_espera = Paciente.objects.filter(status='aguardando')
    pacientes_chamados = Paciente.objects.filter(status='atendimento')
    contexto = {
        'pacientes_espera': pacientes_espera,
        'pacientes_chamados': pacientes_chamados,
    }
    return render(request, 'recepcao.html', contexto)
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após o login
        else:
            error_message = 'Usuário ou senha incorretos.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('login') # Redireciona para a página de login após o logout
    
def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Redireciona para a página de login após o cadastro
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})