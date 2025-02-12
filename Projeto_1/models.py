from django.db import models;

class Paciente(models.Model):
    Nome = models.CharField(max_length=100)
    CPF = models.CharField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    Data_Nascimento = models.DateTimeField(auto_now_add=True)
    Endereco = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Nome} - {self.telefone} - {self.CPF} - {self.Data_Nascimento} - {self.Endereco}"

class Cores(models.Model):
    Nome = models.CharField(max_length=15)
    
'teste'
'teste'