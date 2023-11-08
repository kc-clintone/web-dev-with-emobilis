from django.db import models

class Image(models.Model):
	title=models.CharField(max_length=250)
	image=models.ImageField(upload_to='images/')
