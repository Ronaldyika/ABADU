from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Gallery(models.Model):
    title = models.CharField(max_length=20)
    image = models.FileField(upload_to='media')
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add='true')

class Messages(models.Model):
    sender = models.ForeignKey(Customer,on_delete=models.CASCADE)
    content = models.TextField()
    sent_date = models.DateField(auto_now_add='true')


    def __str__(self):
        return self.sender

class blog(models.Model):
    image = models.ImageField(upload_to='media')
    description = models.TextField()