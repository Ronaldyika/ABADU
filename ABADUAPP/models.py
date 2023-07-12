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

class Messages(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    sent_date = models.DateField(auto_now_add='true')


    def __str__(self):
        return self.sender

class blogpost(models.Model):
    image = models.ImageField(upload_to='media')
    description = models.TextField()