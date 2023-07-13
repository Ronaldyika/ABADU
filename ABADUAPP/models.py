from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=255)

    def __str__(self):
        return self.room_name
class Admininfo(User):

    def __str__(self):
        return self.username

class Gallery(models.Model):
    title = models.CharField(max_length=20)
    image = models.FileField(upload_to='media')
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add='true')

class Message(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE, default='')
    sender = models.CharField(max_length=255)
    message = models.TextField()

class blogpost(models.Model):
    image = models.ImageField(upload_to='media')
    description = models.TextField()