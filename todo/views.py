from django.shortcuts import render, redirect
from django.views import View
from .models import Todo

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        todos = Todo.objects.all()
        context = { "todos": todos}    # todos の中には複数データが入っている

        return render(request, "todo/index.html", context)   # template 以下を読む （setting.py で指定している）
    
    def post(self, request, *args, **kwargs):
        todo = Todo(content=request.POST["content"], deadline=request.POST["deadline"])
        todo.save()

        return redirect("todo:index")


index = IndexView.as_view()

