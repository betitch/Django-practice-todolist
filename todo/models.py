from django.db import models

# Create your models here.
class Todo(models.Model):    # フィールドを作る   id は自動的に振られる。

    content = models.CharField(max_length=100)
    
    deadline = models.DateField()

    # done = models.BooleanField()