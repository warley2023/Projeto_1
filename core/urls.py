from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('paciente/adicionar/', views.adicionar_paciente, name='adicionar_paciente'),
    path('paciente/editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('paciente/deletar/<int:id>/', views.deletar_paciente, name='deletar_paciente'),
    path('paciente/monitorar/', views.monitorar_paciente, name='monitorar_paciente'),
    path('chamar_paciente/<int:paciente_id>/', views.chamar_paciente, name='chamar_paciente'),
    path('paciente_atendimento/<int:paciente_id>/', views.paciente_atendimento, name='paciente_atendimento'),
    path('paciente_evadiu/<int:paciente_id>/', views.paciente_evadiu, name='paciente_evadiu'),
    path('paciente_alta/<int:paciente_id>/', views.paciente_alta, name='paciente_alta'),
    path('recepcao/', views.recepcao, name='recepcao'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('mensagens/', views.my_view, name='my_view')
]