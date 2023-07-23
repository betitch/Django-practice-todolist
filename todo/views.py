from django.shortcuts import render, redirect
from django.views import View
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        todos = Todo.objects.all()
        context = { "todos": todos}    # todos の中には複数データが入っている

        return render(request, "todo/index.html", context)   # template 以下を読む （setting.py で指定している）
    
    def post(self, request, *args, **kwargs):
        """
        todo = Todo(content=request.POST["content"], deadline=request.POST["deadline"])   バリデーションチェックされてない
        todo.save()
        """
        form = TodoForm(request.POST)        # 継承する forms.ModelForm に取る引数の情報が設定されている
        if form.is_valid():                  # models → views の間に forms を挟む感じ
            form.save()
        else:
            print(form.errors)
            messages.error(request, form.errors)


        return redirect("todo:index")


index = IndexView.as_view()

# 個別表示のビュー
class Singleview(View):
    def get(self, request, pk, *args, **kwargs):
        
        todo = Todo.objects.filter(id=pk).first()    # 配列で取ってくるので、１個でも first が必要、 無いと for ループを回す必要がある
        context ={ "todo":todo }

        return render(request, "todo/single.html", context)


single = Singleview.as_view()
        

# 削除のビュー       
class DeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        print("削除")
        print(pk)

        todo = Todo.objects.filter(id=pk).first()
        todo.delete()

        return redirect("todo:index")

delete = DeleteView.as_view()



class EditView(View):

    def post(self, request, pk, *args, **kwargs): #  pk 編集対象のid
        print("編集")
        print(pk)

        todo = Todo.objects.filter(id=pk).first()   # 編集対象のTodoを特定する

        form = TodoForm(request.POST, instance=todo) # instance に編集対象の Todo を指定
        
        if form.is_valid():                  # models → views の間に forms を挟む感じ
            form.save()
        else:
            print(form.errors)
            messages.error(request, form.errors)

        return redirect("todo:index")

edit = EditView.as_view()

# Todo の完了、未完を切り替えるビュー
class Doneview(View):
    def post(self, request, pk, *args, **kwargs): #  pk 編集対象のid
        print("切り替え")
        todo = Todo.objects.filter(id=pk).first() 
        # todo.done = True                           # バリデーションは不要

        todo.done = not todo.done                    # デフォルトで False なので、ボタンを押すと True になる

        todo.save()

        return redirect("todo:index")
    
done = Doneview.as_view()

