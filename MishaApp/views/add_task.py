#add every view to urls.py, I guess
#also, add a template for every view
from datetime import timezone

from django.shortcuts import render, redirect
from ..models import Task
from datetime import datetime

def add_task(request):
    if request.method == "POST":
        task_text = request.POST.get("task", "").strip()

        if task_text:
            # for now, just print it or save later
            print("TASK:")
            print(task_text)

            task = Task()
            task.text = task_text
            task.taskDescription=task_text
            task.addDate = datetime.now()
            task.save()

            # redirect prevents form resubmission
            return redirect("/added")

    # GET request (or invalid POST)
    return render(request, "add_task.html")
