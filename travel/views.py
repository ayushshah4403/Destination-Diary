from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def destinations(request):
    if request.method == "POST":        
        data = request.POST
        destination_name  = data.get('destination_name')
        destination_description  = data.get('destination_description')
        destination_image = request.FILES.get('destination_image')
        
        Destination.objects.create(
            destination_name = destination_name,
            destination_description = destination_description,
            destination_image = destination_image
        )
        
        return redirect('/')
    query_set = Destination.objects.all()
    context = {'destinations' : query_set, 'title' : 'Destination Diary'}
    
    return render(request, 'home.html', context)


def update_destination(request, id):
    queryset = Destination.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        destination_name  = data.get('destination_name')
        destination_description  = data.get('destination_description')
        destination_image = request.FILES.get('destination_image')
        queryset.destination_name = destination_name
        queryset.destination_description =  destination_description
        
        if destination_image:
            queryset.destination_image = destination_image
        
        queryset.save()
        return redirect('/')
    context = {'destination' : queryset, 'title' : 'Update Destination'}
    return render(request, "update_destination.html", context)


def delete_destination(request, id):
    query_set = Destination.objects.get(id = id)
    query_set.delete()
    return redirect('/')

#Login Page

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not (User.objects.filter(username = username).exists()):
            messages.info(request, "Invalid username")
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)
        
        if user is None:
            messages.info(request, "Incorrect Password!")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/')
            
    context = {'title':'Login'}
    return render(request, "login.html", context)

#Register Page

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('/register/')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()
        messages.info(request, 'Account created successfully')
        return redirect('/login/')
    context = {'title':'Register', 'styling-info' : 'alert alert-info', 'styling-warning' : 'alert alert-warning'}
    return render(request, "register.html", context)

#Logout Page

def logout_page(request):
    logout(request)
    return redirect('/login/')