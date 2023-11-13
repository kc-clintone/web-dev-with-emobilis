from django import forms
from .models import ToDo

clsss TaskForm(forms.ModelForm):
	class Meta:
		model=ToDo
		fields=['todo', 'description']
