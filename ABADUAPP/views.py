from django.shortcuts import render
from .models import Customer,Messages,Gallery,blog
# Create your views here.

def index(request):
    return render(request,'main/index.html')

def registercustomer(request):
    return render(request,'customer/register.html')


def logincustomer(request):
    return render(request,'customer/login.html')

def registeradmin(request):
    return render(request,'adminsite/register.html')

def signinadmin(request):

    return render(request,'adminsite/login.html')

def customergallery(request):
    posts = Gallery.objects.all()
    cards = blog.objects.all()
    context = {
        'posts':posts,
        'cards':cards
    }

    return render(request,'customer/gallery.html',context)