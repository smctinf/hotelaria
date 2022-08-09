from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('kpi/', views.kpi, name='kpi'),
    path('regiao/', views.regiao, name='regiao'),
    path('regiao/listar', views.listarRegiao, name='listagem_regiao'),
    path('hospedagem/', views.hospedagem, name='hospedagem'),
    path('hospedagem/editar/<id>', views.editarHospedagem, name='editar_hospedagem'),
    path('hospedagem/listar', views.listarHospedagem, name='listagem_hospedagem'),
    path('ocupacao/', views.ocupacao, name='ocupacao'),
    path('ocupacao/listar', views.listarOcupacao, name='listagem_ocupacao')
    
    
]
