from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # at /blog/ or / depending on project urls
]
