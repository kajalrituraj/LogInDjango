from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')

def HomePage(request):
    print(request)
    return render(request, 'home.html')


def SignUpPage(request):
    if request.method == 'POST':
        userName = request.POST.get('userName')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        Cnfpass = request.POST.get('confirmPass')

        if pass1 != Cnfpass:
            return HttpResponse("your password and confirm password are not same")
        else:
            my_user = User.objects.create_user(userName, email, pass1)
            my_user.save()
            return redirect('login')
        # print(uname,email,pass1,Cnfpass)

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        userName = request.POST.get('userName')
        pass1 = request.POST.get('pass1')
        user = authenticate(request, username=userName, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("incorrect")
    return render(request, 'login.html')
# Create your views here.


def LogOutPage(request):
    logout(request)
    return redirect('login')
