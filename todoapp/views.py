from django.shortcuts import render
from .models import ToDoListItem
from django.http import HttpResponseRedirect

# Create your views here.
def todoappView(request):
    all_todo_items = ToDoListItem.objects.all()
    return render(request, 'todolist.html',{'all_items':all_todo_items})

def addTodoView(request):
    x = request.POST['content']
    new_item = ToDoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    y = ToDoListItem.objects.get(id= i)
    y.delete()
    messages.info(request, "item removed !!!")
    return HttpResponseRedirect('/todoapp/')