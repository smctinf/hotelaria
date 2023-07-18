from django.shortcuts import render
from .forms import Form_Login

def login(request):
    if request.method == "POST":
       print(request)
    context = {
        'form' : Form_Login,
    }
    return render(request, 'login.html', context) 
