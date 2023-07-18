from django.urls import path, include
from . import views

app_name = 'autenticacao'
urlpatterns = [
    path('login/', views.login, name='login'),

    #path('password_reset', views.password_reset, name='password_reset'),
    #path('cadastrar', views.cadastrar, name='cadastrar'),
]
