# views.py
from django.shortcuts import render
from django.http import HttpResponse
import subprocess

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
    import json

    try:
        json_data = json.loads(output.decode('utf-8'))
        # Extract and process information from the JSON data as needed
        # Example: vulnerabilities = json_data['results']
        vulnerabilities = []  # Replace this with your parsing logic
        return vulnerabilities
    except json.JSONDecodeError as e:
        # Handle JSON parsing errors
        print(f"Error parsing Bandit output: {e}")
        return []
