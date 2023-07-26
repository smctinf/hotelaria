from django.contrib import admin
from django.urls import path, include

app_name = 'hotelaria'
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    
    path('', include('contas.urls')),
    path('', include('ocupacao.urls'))
]
