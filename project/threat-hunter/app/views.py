from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .forms import ExtensionUploadForm, CreateUserForm, LoginForm
#code analysi with bandit
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import subprocess
import json

# code analysis with AI
import openai

@login_required
def analyse_with_ai(request):
    if request.method == 'POST':
        user_code = request.POST.get('user_code')

        openai.api_key = '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'
        prompt = f"Review the following code and identify any syntax errors, potential security issues or improvements:\n\n{user_code}"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0.7,
            n=1,
        )

        review_result = response.choices[0].text.strip()
        return render(request, 'airesult.html', {'review_result': review_result})

    return render(request, 'aiform.html')

@login_required
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

@login_required
def home(request):
    subscribed = False
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


@login_required
def result_page(request, vulnerabilities):
    return render(request, 'result_page.html', context={'vulnerabilities': vulnerabilities})

@login_required
def about(request):
    return render(request, 'about.html')

# -----user creation and authentication----

def signup(request):
    this_form = CreateUserForm()

    if request.method == "POST":
        this_form = CreateUserForm(request.POST)
        if this_form.is_valid():
            this_form.save()

            return redirect('signin')
    return render(request, 'signup.html', context = {'form': this_form})

def signin(request):
    this_form = LoginForm()
    if request.method == "POST":
        this_form = LoginForm(request, data=request.POST)
        if this_form.is_valid():
            this_username = request.POST.get('username')
            this_password = request.POST.get('password')

            this_user = authenticate(request, username=this_username, password=this_password)

            if this_user is not None:
                auth.login(request, this_user)
                return redirect('home')

    return render(request, 'signin.html', context = {'form':this_form})

def signout(request):
    auth.logout(request)
    return redirect('signin')
