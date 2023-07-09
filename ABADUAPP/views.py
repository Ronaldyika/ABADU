from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'base/base.html')

def registercustomer(request):
    return render(request,'customer/register.html')