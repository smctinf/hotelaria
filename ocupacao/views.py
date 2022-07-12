from django.shortcuts import render

from ocupacao.forms import Form_Hospedagem, Form_Ocupacao, Form_Regiao
from django.contrib.auth.decorators import login_required

from ocupacao.models import Ocupacao

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def regiao(request):
    form=Form_Regiao(initial={'user':request.user})
    if request.method=='POST':
        form=Form_Regiao(request.POST)
        if form.is_valid():
            form.save()
            form=Form_Regiao(initial={'user':request.user})

    context={
        'form': form
    }
    return render(request, 'forms.html', context)

@login_required
def hospedagem(request):
    form=Form_Hospedagem(initial={'user':request.user})
    if request.method=='POST':
        form=Form_Hospedagem(request.POST)
        if form.is_valid():
            form.save()
            form=Form_Hospedagem(initial={'user':request.user})

    context={
        'form': Form_Hospedagem(initial={'user':request.user})
    }
    return render(request, 'forms.html', context)

@login_required
def ocupacao(request):
    form=Form_Ocupacao(initial={'user':request.user})
    if request.method=='POST':
        form=Form_Ocupacao(request.POST)
        if form.is_valid():
            form.save()
            form=Form_Ocupacao(initial={'user':request.user})

    context={
        'form': Form_Ocupacao(initial={'user':request.user})
    }
    return render(request, 'forms.html', context)

@login_required
def listarOcupacao(request):
    context={
        'listar': Ocupacao.objects.all()
    }
    return render(request, 'listar.html', context)