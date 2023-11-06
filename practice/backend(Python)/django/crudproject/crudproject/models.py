from django.db import models

class Student(models.Model):
	name = models.CharField(max_length=20, blank=False, null=False)
	email = models.EmailField()
	age = models.IntegerField()
	gender = models.CharField(max_length=7, blank=False, null=False)


def __str__(self):
	return self.name
