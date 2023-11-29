from django.shortcuts import render, redirect
from .forms import ExtensionUploadForm
from .models import UploadedExtension
from django.http import HttpResponse


def upload_extension(request):
    if request.method == 'POST':
        form = ExtensionUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Add bug detection logic here
            return redirect('result_page')
    else:
        form = ExtensionUploadForm()

    return render(request, 'upload_extension.html', {'form': form})


def signup(request):
    pass

def signin(request):
    pass
