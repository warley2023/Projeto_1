from django.db import models

class paciente(models.Model):
    nome = models.CharField(max_length=100)
    temperatura = models.FloatField()
    pressao = models.CharField(max_length=20)
    urgencia = models.CharField(
        max_length=10,
        choices=[("Verde", "Verde"), ("Amarelo", "Amarelo"), ("Vermelho", "Vermelho")]
    )

    def __str__(self):
        return self.nome

