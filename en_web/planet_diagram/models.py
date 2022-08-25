from django.db import models

# Create your models here.

class Planet(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(blank = True, null = True, upload_to = 'planet_image')

class Comment(models.Model):
    comment = models.CharField(max_length = 100)
    planet = models.ForeignKey(Planet, on_delete = models.CASCADE)

    def __self__(self):
        return self.comment