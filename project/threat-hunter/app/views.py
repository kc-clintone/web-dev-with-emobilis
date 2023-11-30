from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

def home(request):
    

    return render(request, 'index.html', context = {'form':this_form})

def dashboard(request):
    return render(request, 'dashboard.html')

def signup(request):
    this_form = CreateUserForm()

    if request.method == "POST":
        this_form = CreateUserForm(request.POST)
        if this_form.is_valid():
            this_form.save()
            return redirect("signin")

    return render(request, 'signup.html', context = {'form': this_form})

def signin(request):
    this_form = LoginForm()

    if request.method == "POST":
        this_form = LoginForm(request, data=request.POST)
        if this_form.is_vali():
            username = request.POST.get('username')
    return render(request, 'signin.html')
