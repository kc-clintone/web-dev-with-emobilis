from django.db import models

class Todo(models.Model):

    title=models.CharField(max_length=30)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:

        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'