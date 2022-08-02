from django.shortcuts import render

from ocupacao.forms import Form_Hospedagem, Form_Ocupacao, Form_Regiao
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ocupacao.models import Ocupacao, Hospedagem, Regiao
from django.db.models import Q

from hotelaria.decorators import membro_secretaria_required

# Create your views here.
@membro_secretaria_required
def index(request):
    return render(request, 'index.html')

@membro_secretaria_required
def kpi(request):
    if request.method == 'POST':
        try:
            hospedagem_id=request.POST['hospedagem']
        except:
            hospedagem_id=None
        try:
            regiao=request.POST['regiao']
        except:
            regiao=None
        try:
            complexQuery=Q(dt_inclusao__range=[request.POST['dt_inclusao'], request.POST['dt_inclusao_f']])|Q(hospedagem_id=hospedagem_id)|Q(hospedagem__regiao_id=regiao)
            ocupacao=Ocupacao.objects.filter(complexQuery).order_by('hospedagem__regiao_nome', 'hospedagem__nome')
        except Exception as e:
            messages.error(request, 'Erro ao gerar KPI ---> '+str(e))   
            ocupacao=None         
        # ocupacao=Ocupacao.objects.filter(dt_1__range=[request.POST['dt_inclusao'], request.POST['dt_inclusao_f']])        
        context={
            'filtro': True,
            'ocupacoes': ocupacao,
            'hospedagens': Hospedagem.objects.all(),
            'regioes': Regiao.objects.all(),
        }
    else:
        context={
            'filtro': False,            
            'hospedagens': Hospedagem.objects.all(),
            'regioes': Regiao.objects.all(),
        }
    return render(request, 'kpi.html', context)

@membro_secretaria_required
def regiao(request):
    form=Form_Regiao(initial={'user':request.user})
    if request.method=='POST':
        form=Form_Regiao(request.POST)
        if form.is_valid():
            form.save()
            form=Form_Regiao(initial={'user':request.user})
            messages.success(request, 'Região registrada com sucesso no banco de dados!')

    context={
        'form': form
    }
    return render(request, 'forms.html', context)

@membro_secretaria_required
def hospedagem(request):
    form=Form_Hospedagem(initial={'user':request.user})
    if request.method=='POST':
        form=Form_Hospedagem(request.POST)
        if form.is_valid():
            form.save()
            form=Form_Hospedagem(initial={'user':request.user})
            messages.success(request, 'Hospedagem cadastrada com sucesso no banco de dados!')
    context={
        'form': Form_Hospedagem(initial={'user':request.user})
    }
    return render(request, 'forms.html', context)

@membro_secretaria_required
def ocupacao(request):
    form=Form_Ocupacao(initial={'user':request.user})
    if request.method=='POST':
        form=Form_Ocupacao(request.POST)
        if form.is_valid():
            form.save()
            form=Form_Ocupacao(initial={'user':request.user})
            messages.success(request, 'Registro de ocupação realizada com sucesso no banco de dados!')
    context={
        'form': Form_Ocupacao(initial={'user':request.user})
    }
    return render(request, 'forms.html', context)

@membro_secretaria_required
def listarOcupacao(request):
    context={
        'listar': Ocupacao.objects.all().order_by('hospedagem_id', 'hospedagem__nome')
    }
    return render(request, 'listar.html', context)