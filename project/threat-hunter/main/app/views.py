from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'app/index.html')

def dashboard(request):
    return render(request, 'app/dashboard.html')

def signup(request):
    return render(request, 'app/signup.html')

def signin(request):
    return render(request, 'app/signin.html')
