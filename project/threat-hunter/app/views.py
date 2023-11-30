from django.shortcuts import render, redirect
from . forms import CreateUserForm

def home(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def signup(request):
    this_form = CreateUserForm()

    if request.method == "POST"
        this_form = CreateUserForm(request.POST)
        if this_form.is_valid():
            this_form.save()
            return redirect("signin")

    return render(request, 'signup.html', context = {'form': this_form})

def signin(request):
    return render(request, 'signin.html')
