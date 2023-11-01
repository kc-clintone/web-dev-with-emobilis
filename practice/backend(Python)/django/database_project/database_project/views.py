from django.shortcuts import render
from database_project.forms import userDetailsForm

def forms(request):
    this_form=userDetailsForm()
    return render(request, 'index.html',{'form': this_form})