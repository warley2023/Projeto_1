# Generated by Django 5.1.6 on 2025-02-22 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_paciente_data_hora_entrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='urgencia',
            field=models.CharField(choices=[('Azul', 'Azul'), ('Verde', 'Verde'), ('Amarelo', 'Amarelo'), ('Vermelho', 'Vermelho')], max_length=10),
        ),
    ]
