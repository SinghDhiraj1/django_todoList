from django.shortcuts import render, redirect
from .models import ToDo


# Create your views here.

def index(request):
    todo = ToDo.objects.all()
    if request.method == 'POST':
        new_todo = ToDo(
            title=request.POST['title']
        )
        new_todo.save()
        return redirect('/')

    return render(request, 'index.html', {'todos': todo})


def delete(request, pk):
    todo = ToDo.objects.get(id=pk)
    todo.delete()
    return redirect('/')
