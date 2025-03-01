from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World! This came from the index view')

def list(request):
    # return HttpResponse('This is from /recipes/list')
    ctx = {
        "tasks": [
            "task 1",
            "task 2",
            "task 3",
            "task 4"
        ]
    }
    return render(request, 'templates/base.html',ctx)