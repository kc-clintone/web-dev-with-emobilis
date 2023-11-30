import subprocess

def analyze_code_with_bandit(file_path):
    command = f"bandit -r {file_path}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        # Handle vulnerabilities - you can log them or take appropriate actions
        print(f"Bandit found vulnerabilities: {output.decode('utf-8')}")
    else:
        print("No vulnerabilities found.")

