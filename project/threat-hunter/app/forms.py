from django.contrib.auth.forms import UserCreationForm
from django.conrrib.auth.models from User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fielsd = ['username, 'email' 'password1', password2']
