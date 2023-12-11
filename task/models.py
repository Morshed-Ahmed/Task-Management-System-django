from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.TextField(max_length=500)
    date = models.DateField()
    categories = models.ManyToManyField(Category)
    is_completed = models.BooleanField(default=False)


    def __str__(self):
        return self.taskTitle
    