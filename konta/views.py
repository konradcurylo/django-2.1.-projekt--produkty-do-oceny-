from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def rejestracja(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'konta/rejestracja.html',{'error':'Taki użytkownik już istnieje!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
             return render(request, 'konta/rejestracja.html',{'error':'Podane hasła muszą być takie same.'})

    else:
        return render(request,'konta/rejestracja.html')






def logowanie(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'konta/logowanie.html',{'error':'Nazwa użytkownika albo hasło są niepoprawne.'})

    else:
        return render(request,'konta/logowanie.html')

def wylogowanie(request):
        if request.method == 'POST':
            auth.logout(request)
            return redirect('home')
    
