from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Gallery(models.Model):
    title = models.CharField(max_length=20)
    image = models.FileField(upload_to='media')
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add='true')

class blogpost(models.Model):
    image = models.ImageField(upload_to='media')
    description = models.TextField()