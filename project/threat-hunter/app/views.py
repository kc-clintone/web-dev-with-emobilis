from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, ExtensionUploadForm
from . import code_analysis
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
import subprocess

def home(request):
    if request.method == 'POST':
        this_form = ExtensionUploadForm(request.POST, request.FILES)
        if this_form.is_valid():
            home = this_form.save()
            # Perform static code analysis using Bandit
            analyze_code_with_bandit(uploaded_extension.file.path)
            #return redirect('result_page')
    else:
        this_form = ExtensionUploadForm()

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
