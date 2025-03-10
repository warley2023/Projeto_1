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

    # Adicionando o método para definir a prioridade da urgência (ordem numérica)
    @property
    def urgencia_order(self):
        """
        Retorna a prioridade numérica para cada nível de urgência, para ordenar corretamente.
        Quanto menor o número, maior a prioridade.
        """
        prioridade = {
            "vermelho": 1,  # Prioridade 1
            "laranja": 2,   # Prioridade 2
            "amarelo": 3,   # Prioridade 3
            "verde": 4,     # Prioridade 4
            "azul": 5       # Prioridade 5
        }
        return prioridade.get(self.urgencia, 5)  # Se não encontrar, assume a menor prioridade

    class Meta:
        # Remover a ordenação por urgencia_order, já que não é um campo no banco de dados
        ordering = ['urgencia', 'data_hora_entrada']  # Ordena pela urgência e hora de entrada

    def get_urgencia_color(self):
        """
        Retorna uma cor associada à urgência do paciente para visualização.
        """
        cores = {
            'azul': 'blue',
            'verde': 'green',
            'amarelo': 'yellow',
            'laranja': 'orange',
            'vermelho': 'red'
        }
        return cores.get(self.urgencia, 'gray')  # Retorna a cor associada ou cinza por padrão

    def __str__(self):
        """
        Método que retorna o nome do paciente seguido do texto da urgência.
        """
        return f"{self.nome} - {self.get_urgencia_display()}"  # Nome e descrição da urgência


class Area(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
