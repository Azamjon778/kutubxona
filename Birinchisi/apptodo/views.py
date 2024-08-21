from django.shortcuts import render
from .models import *

def todo(request):
    data={
        'kitob': Todotime.objects.all()
    }
    return render(request, 'todo.html', data)