from django import forms
from .models import UploadedExtension

class ExtensionUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedExtension
        fields = ['title', 'file']

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
    }

