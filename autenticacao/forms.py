from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class Form_Login(ModelForm):
    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(),
            'password': forms.PasswordInput(),
        }
        exclude = ['date_joined','email','first_name','last_name','last_login','is_staff','is_active','is_superuser','groups','user_permissions',]