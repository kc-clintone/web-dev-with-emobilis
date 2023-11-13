from django import forms
from .models import ToDo

clsss TodosForm(forms.ModelForm):
	class Meta:
		model=ToDo
		fields=['todo', 'description']
