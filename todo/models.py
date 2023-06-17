from django.db import models

# Create your models here.
class Todo(models.Model):    # フィールドを作っていく

    content = models.CharField(max_length=100)
    
    deadline = models.DateField()