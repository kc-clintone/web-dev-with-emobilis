from django.db import models

class Image(models.Model):
	title=CharField(max_length=250)
	image=ImageField(upload_to='images/')
