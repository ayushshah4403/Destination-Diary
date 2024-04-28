from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Destination(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    destination_name = models.CharField(max_length = 100)
    destination_description = models.TextField()
    destination_image = models.ImageField(upload_to = 'destinations')