from django.db import models
from django.utils import timezone


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length = 100)
    progress = models.FloatField()
    date = models.DateTimeField(auto_now_add = True)
