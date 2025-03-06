from django.urls import path
from .views import areaAPIlistar

urlpatterns =[
    path('areas/listar/', areaAPIlistar.as_view()),
]