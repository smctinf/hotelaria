from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from hotelaria.decorators import membro_secretaria_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context = {
                'error': True,
            }
            return render(request, 'auth/login.html', context) 
    return render(request, 'auth/login.html')

@membro_secretaria_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'auth/logout.html')
    return redirect('auth/login')    
