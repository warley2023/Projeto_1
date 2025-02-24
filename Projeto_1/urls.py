from django.contrib import admin
from django.urls import path
from core.views import  login_view, listar_paciente, adicionar_paciente, editar_paciente, deletar_paciente, monitorar_paciente, index

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('paciente/', listar_paciente, name='listar_paciente'),
    path('paciente/adicionar/', adicionar_paciente, name='adicionar_paciente'),
    path('paciente/editar/<int:id>/', editar_paciente, name='editar_paciente'),
    path('paciente/deletar/<int:id>/', deletar_paciente, name='deletar_paciente'),
    path('paciente/monitorar/', monitorar_paciente, name='monitorar_paciente'),
]