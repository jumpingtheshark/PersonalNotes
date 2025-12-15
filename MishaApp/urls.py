from django.urls import path
from . import views
from .views.home import home
from .views.add_task import add_task
from .views.item_added import item_added


urlpatterns = [
    path("", home, name="home"),  # at /blog/ or / depending on project urls
    path("add/",  add_task, name="add_task"),
    path("added/", item_added, name="item_added"),
]
