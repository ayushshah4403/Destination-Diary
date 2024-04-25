from django.db import models

# Create your models here.

class Destination(models.Model):
    destination_name = models.CharField(max_length = 100)
    destination_description = models.TextField()
    destination_image = models.ImageField(upload_to = 'destinations')