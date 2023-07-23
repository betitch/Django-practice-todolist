from django.db import models

# Create your models here.      モデルを編集したら　マイグレーションが必要
class Todo(models.Model):    # フィールドを作る   id は自動的に振られる。

    content = models.CharField(max_length=100)
    
    deadline = models.DateField()

    done = models.BooleanField(default=False)    # やったかどうかの記録（フィールド入力必須 null 禁止）

