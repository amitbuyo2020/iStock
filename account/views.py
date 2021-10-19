from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        redirect('home')
    
    else:
        error = "Login Failed. Please try again."

    context = {
        'error': error
    }
    return render(request, 'account/login.html', context)