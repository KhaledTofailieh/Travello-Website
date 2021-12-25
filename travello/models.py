from django.db import models


# Create your models here.

class Destination(models.Model):

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    img_url = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)

