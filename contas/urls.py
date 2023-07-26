from django.urls import path, include
from . import views

app_name = 'contas'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    #path('password_reset', views.password_reset, name='password_reset'),
    #path('cadastrar', views.cadastrar, name='cadastrar'),
]
