from django.shortcuts import redirect, render
from django.http import HttpResponse
from store.models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request,'login.html')   

def log(request):
    username = request.GET.get('a1')
    password = request.GET.get('a2')
    
    # Use filter() to handle multiple objects
    users = man.objects.filter(username=username)
    
    if users.exists():
        # Check if any of the returned users have the correct password
        user = users.filter(password=password).first()
        
        if user:
            # User exists and password is correct
            messages.success(request, 'Logged in successfully!')
            return redirect('home')  # Ensure 'home' matches the name of your home URL pattern
        else:
            # Password is incorrect
            messages.error(request, 'Password is incorrect!')
            return redirect('login')  # Ensure 'login' matches the name of your login URL pattern
    else:
        # User does not exist, create a new user
        new_user = man(username=username, password=password)
        new_user.save()
        messages.success(request, 'User created successfully!')
        return redirect('home')  # Ensure 'home' matches the name of your home URL pattern

