from django.db import models

# Create your models here.


class Task (models.Model):
    taskDescription = models.CharField(max_length=100)
    addDate = models.DateField()
    done= models.BooleanField(default=False)
    def __str__(self):
        return self.taskDescription

