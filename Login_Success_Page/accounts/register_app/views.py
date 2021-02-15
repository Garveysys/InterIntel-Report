from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:    
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account has been created for ' + user) 
                return redirect('login')

            

    # pass it in to our template and render it
    context = {'form':form}
    # pass the name of the template to render  
    return render(request, 'register_app/register.html', context) 

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR Password is incorrect')
                

        context= {}
        return render(request, 'register_app/login.html', context)    

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'register_app/index.html', context)    