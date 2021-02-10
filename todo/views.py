from django.shortcuts import render,redirect
from django.http import HttpResponse
from todo.models import Todo
from todo.forms2 import TodoModel
# Create your views here.
def index(request):
    data = Todo.objects.all()
    form=TodoModel()
    if request.method=="POST":
        form=TodoModel(request.POST)
        form.save()
    context={'data':data,'form':form}
    return render(request,'list.html',context)

def update(request,id):
    data=Todo.objects.get(id=id)
    form=TodoModel(instance=data)
    if request.method=="POST":
        form=TodoModel(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'update.html',context)

