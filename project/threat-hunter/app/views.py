from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, ExtensionUploadForm
#code analysi with bandit
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
import subprocess
import json
#code analysis with AI
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

def analyze_code_with_codebert(code_snippet):
    model_name = "microsoft/codebert-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    tokens = tokenizer.encode_plus(code_snippet, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        embeddings = model(**tokens).last_hidden_state


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
    subscribed = False
    if request.method == 'POST':
        this_form = ExtensionUploadForm(request.POST, request.FILES)
        if this_form.is_valid():
            home = this_form.save()
            if subscribed == True:
                # Deeper code analysis using BERT
                code_content = uploaded_extension.file.read().decode('utf-8')
                analyze_code_with_codebert(code_content)
            else:
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
