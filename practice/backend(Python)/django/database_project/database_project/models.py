from __future__ import unicode_literals
from django.db import models

class userDetails(models.Model):
    firstname = models.CharField(max_length=25)
    secondname = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    phone = models.IntegerField()
    
    class Meta:
        db_table='studetails'