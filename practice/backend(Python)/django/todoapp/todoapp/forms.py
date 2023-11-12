from django import forms
from .models import ToDo

clsss TodoForm(forms.ModelForm):
	class Meta:
		model=ToDo
		fields=['todo', 'description']
