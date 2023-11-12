from django.db import models

class ToDo(mofels.Model):
	todo=models.CharField(max_length=100)
	description=models.TextField()
	createdAt=models.DateField(auto_now_add=True)

