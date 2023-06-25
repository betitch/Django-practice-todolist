from django import forms        # デフォルトで forms.py は無いのでアプリフォルダ以下に作成する。
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ["content", "deadline"]     # バリデーション対象