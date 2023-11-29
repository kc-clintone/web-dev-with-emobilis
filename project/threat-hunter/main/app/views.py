from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')
