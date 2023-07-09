from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'main/index.html')

def registercustomer(request):
    return render(request,'customer/register.html')