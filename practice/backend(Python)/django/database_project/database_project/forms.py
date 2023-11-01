from django import forms
from database_project.models import userDetails

class userDetailsForm(forms.ModelForm):
    
    class Meta:
        model = userDetails
        fields = '__all__'
