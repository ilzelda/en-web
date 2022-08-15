from django.db import models

# Create your models here.

class Diary(models.Model):
    date = models.DateField(auto_now_add = True)
    description = models.TextField()

    def __self__(self):
        return self.description