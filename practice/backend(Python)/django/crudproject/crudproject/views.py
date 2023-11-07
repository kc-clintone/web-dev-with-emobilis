from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Student

def home(request):
	data = Student.objects.all()
	return render(request, 'index.html', {'data':data})

def insertData(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		age = request.POST.get('age')
		gender =request.POST.get('gender')

		createStud = Student(name=name, email=email, age=age,
gender=gender)
		createStud.save()
		return redirect('/')
	else:
		return render(request, 'index.html')


def updateData(request, id):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		age = request.POST.get('age')
		gender =request.POST.get('gender')

		updateStud = Student.objects.get(id=id)
		updateStud.name=name
		updateStud.email=email
		updateStud.age=age
		updateStud.gender=gender
		updateStud.save()
		return redirect('/')
	else:
		data = Student.objects.get(id=id)
		return render(request, 'edit.html', {'data': data})

def deleteData(request, id):
	deleteStud = Student.objects.get(id=id)
	deleteStud.delete()
	return redirect('/')

def handleLogout(request):
	logout(request, 'login.html')


def handleLogin(request):
	if request.method == 'POST':
		this_username=request.POST.get('username')
		this_password=request.POST.get('password')
		this_user=authenticate(username=this_username,
password=this_password)
		if this_user is not None:
			login(request, this_user)
			return redirect('/')
		else:
			return redirect('/login')
	return render(request, 'login.html')
