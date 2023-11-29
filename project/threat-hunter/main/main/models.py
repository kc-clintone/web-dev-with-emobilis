from django.db import models

class UploadedExtension(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.title

