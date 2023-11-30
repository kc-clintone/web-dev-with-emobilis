from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, ExtensionUploadForm
#from .code_analysis import analyze_code_with_bandit
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
import subprocess
import json

def analyze_code_with_bandit(file_path):
    command = f"bandit -r {file_path} --format json"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if process.returncode != 0:
        # Handle errors if necessary
        print(f"Bandit analysis failed with error: {error.decode('utf-8')}")
        return []

    # Parse JSON output for detailed results
    vulnerabilities = parse_bandit_output(output)
    return vulnerabilities

def parse_bandit_output(output):
    try:
        json_data = json.loads(output.decode('utf-8'))
        # Extract and process information from the JSON data
        vulnerabilities = []
        for result in json_data['results']:
            vulnerability = {
                'filename': result['filename'],
                'line': result['line'],
                'code': result['code'],
                'issue_text': result['issue_text'],
                'severity': result['issue_severity'],
            }
            vulnerabilities.append(vulnerability)

        return vulnerabilities
    except json.JSONDecodeError as e:
        # Handle JSON parsing errors
        print(f"Error parsing Bandit output: {e}")
        return []


def home(request):
    if request.method == 'POST':
        this_form = ExtensionUploadForm(request.POST, request.FILES)
        if this_form.is_valid():
            home = this_form.save()
            # Perform static code analysis using Bandit
            vulnerabilities = analyze_code_with_bandit(home.file.path)
            return redirect('result_page', vulnerabilities=vulnerabilities)
    else:
        this_form = ExtensionUploadForm()

    return render(request, 'index.html', context = {'form':this_form})


def dashboard(request):
    return render(request, 'dashboard.html')

def result_page(request, vulnerabilities):
    return render(request, 'result_page.html', context={'vulnerabilities': vulnerabilities})

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
