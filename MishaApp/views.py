from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    #return HttpResponse("Hello from the home view!")
    context = {
        "message": "Hello Misha, this is coming from the view!"
    }

    context = {
        "message": "Hello!",
        "count": 42,
        "items": ["a", "b", "c", "wow", "this", "is", "amazing!"],
    }
    return render(request, 'home.html', context)
