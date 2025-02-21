from django.db import models
from django.contrib.auth.models import user


class Paciente(models.Model):
    Nome = models.CharField(max_length=100, null=False)
    CPF = models.CharField(max_length=14, unique=True, null=False) 
    telefone = models.CharField(max_length=15, blank=True, null=True)  
    Data_Nascimento = models.DateField(null=False) 
    Endereco = models.CharField(max_length=255, null=False) 

    def __str__(self):
        return f"{self.Nome} - {self.telefone or 'Sem telefone'} - {self.CPF} - {self.Data_Nascimento} - {self.Endereco}"

class Cores(models.Model):
    Nome = models.CharField(max_length=20, null=False)
    Tempo = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.Nome} - {self.Tempo}"

class Triagem(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE) 
    cor = models.ForeignKey(Cores, on_delete=models.SET_NULL, null=True, blank=True)  
    Pressao = models.CharField(max_length=15, null=False)  
    Temperatura = models.FloatField(null=False, blank=False)  
    Peso = models.FloatField(null=False)  
    Data_Triagem = models.DateTimeField(auto_now_add=True)
    Hora_Triagem = 

    def __str__(self):
        return f"Triagem {self.id} - {self.paciente.Nome} - {self.Pressao} - {self.Temperatura}°C - {self.Peso}kg"

class Meta:
        permissions = [
            ("pode_ver_paciente", "Pode visualizar pacientes"),
            ("pode_editar_paciente", "Pode editar pacientes"),
        ]

if user.has_perm("app.pode_ver_paciente"):
    print("Usuário tem permissão para visualizar pacientes!")