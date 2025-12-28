from django.shortcuts import (
    render,
    redirect,
    get_list_or_404)

from ..models import Task
from datetime import datetime

def show_item(request, id):
    tasks = get_list_or_404(Task, id=id)
    return render(request,
                  "task.html",
                  {'tasks':tasks}
                  )