from django import forms
from django.forms import ModelForm, ValidationError
from .models import *

class Form_Regiao(ModelForm):
    
    class Meta:
        model = Regiao
        widgets={
            'nome': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'user': forms.HiddenInput(attrs={'hidden':True})
        }
        exclude = ['dt_inclusao']


class Form_Hospedagem(ModelForm):
      
    class Meta:
        model = Hospedagem
        widgets={
            'nome': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'user': forms.HiddenInput(attrs={'hidden':True})
        }
        exclude = ['dt_inclusao']

class Form_Ocupacao(ModelForm):
    
    class Meta:
        model = Ocupacao
        widgets={
            'hospedagem': forms.Select(attrs={'class':'form-control mb-3'}),
            'n_uh_ocupados': forms.NumberInput(attrs={'class':'form-control'}),
            'obs': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'dt_1': forms.DateInput(attrs={'placeholder':'', 'type':'date'}),  
            'dt_2': forms.DateInput(attrs={'placeholder':'', 'type':'date'}),  
            'user': forms.HiddenInput(attrs={'hidden':True})
        }
        exclude = ['dt_inclusao']

