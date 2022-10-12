import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'users/user.html')

def register(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pwd1 = request.POST['pwd1']
        pwd2 = request.POST['pwd2']

        if User.objects.filter(username = username):
            messages.error(request, "Username already exists! Try other username")
            return redirect("Users")

        if User.objects.filter(email = email):
            messages.error(request, "Email already registered")
            return redirect("Users")

        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")
        
        if pwd1 != pwd2:
            messages.error(request, "Passwords do not match!")

        

        myuser = User.objects.create_user(username, email, pwd1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()

        messages.success(request, "Account has been sucessfully created")

        return redirect('Users Login')

    return render(request, 'users/register.html')

def loggin(request):

    if request.method == "POST":
        username = request.POST['username']
        pwd1 = request.POST['pwd1']

        user = authenticate(username= username, password = pwd1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "users/user.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('Users')
    
    return render(request, 'users/login.html')

def loggout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('Users')
# Create your views here.
