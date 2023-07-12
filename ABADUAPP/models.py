from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Admininfo(User):

    def __str__(self):
        return self.username

class Gallery(models.Model):
    title = models.CharField(max_length=20)
    image = models.FileField(upload_to='media')
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add='true')

class Message(models.Model):
    sender = models.ForeignKey(Admininfo, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.recipient}: {self.content[:50]}"


    def __str__(self):
        return self.sender

class blogpost(models.Model):
    image = models.ImageField(upload_to='media')
    description = models.TextField()