from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def item_added(request):

    return render(request, 'item_added.html')
