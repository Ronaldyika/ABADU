from django.shortcuts import render

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