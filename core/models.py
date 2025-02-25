#core/models.py
from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    temperatura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)        
    pressao_sistolica = models.IntegerField(null=True, blank=True)  # Pressão sistólica
    pressao_diastolica = models.IntegerField(null=True, blank=True)  # Pressão diastólica
    urgencia = models.CharField(
        max_length=10,
        choices=[
            ("azul", "Azul"),
            ("verde", "Verde"),
            ("amarelo", "Amarelo"),
            ("laranja", "Laranja"),
            ("vermelho", "Vermelho"),
        ],
        null=False,  # Urgência pode ser opcional
        blank=True,
    )
    data_hora_entrada = models.DateTimeField(auto_now_add=True)  # Hora de entrada (automático)
    destino = models.CharField(max_length=50, null=True, blank=True)  # Novo campo
    STATUS_CHOICES = (
        ('aguardando', 'Aguardando'),
        ('atendimento', 'Atendimento'),
        ('evadiu', 'Evadiu'),
        ('alta', 'Alta'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aguardando')
    
    
    def get_urgencia_color(self):
        if self.urgencia == 'azul':
            return 'blue'
        elif self.urgencia == 'verde':
            return 'green'
        elif self.urgencia == 'amarelo':
            return 'yellow'
        elif self.urgencia == 'laranja':
            return 'orange'
        elif self.urgencia == 'vermelho':
            return 'red'
        return 'gray'  # Cor padrão

    def get_urgencia_text(self):
        if self.urgencia == 'azul':
            return 'Azul'
        elif self.urgencia == 'verde':
            return 'Verde'
        elif self.urgencia == 'amarelo':
            return 'Amarelo'
        elif self.urgencia == 'laranja':
            return 'Laranja'
        elif self.urgencia == 'vermelho':
            return 'Vermelho'
        return ''  # Texto padrão
        
    def __str__(self):
        return self.nome