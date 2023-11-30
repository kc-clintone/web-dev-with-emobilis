from .models import UploadedExtension
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class ExtensionUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedExtension
        fields = ['file']

    widgets = {
        'file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
    }
