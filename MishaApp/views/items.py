from django.shortcuts import render, redirect
from ..models import Task
from datetime import datetime


def items(request):
    tasks = Task.objects.all()
    return render(request,
                  'items.html',
                  {'tasks':tasks}
                  )