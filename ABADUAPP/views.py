from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserRegistrationForm,Galleryform,Blogform
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import blogpost,Gallery


# Create your views here.
def index(request):
    return render(request,'index.html')


def RegisterUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("User saved")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'Admin/login/register.html', {'form': form})

def customergallery(request):
    cards = blogpost.objects.all()
    posts = Gallery.objects.all()
    context = {
        'posts':posts,
        'cards':cards
    }

    return render(request,'Users/gallery.html',context)

def upcoming(request):
    cards = blogpost.objects.all()

    context = {
        'cards':cards
    }

    return render(request,'mainblog.html',context)

@login_required()
def admingallery(request):
    cards = blogpost.objects.all()
    posts = Gallery.objects.all()
    context = {
        'posts':posts,
        'cards':cards
    }
    
    return render(request, 'Admin/login/gallery.html', context)

@login_required()
def adminblog(request):
    if request.method == 'POST':
        form = Galleryform(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            gallery = Gallery(title=title, description=description, image=image)
            gallery.save()
            return redirect('admingallery') 
    else:
        form = Galleryform()
    return render(request, 'Admin/login/blog.html', {'form': form})


@login_required()
def deletegallery(request,pk):

    item = Gallery.objects.get(pk=pk)
    item.delete()

    return redirect('admingallery')

@login_required()
def updategallery(request,pk):

    item = get_object_or_404(Gallery, pk=pk)
    if request.method == 'POST':
        form = Galleryform(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('admingallery')
    else:
        form = Galleryform(instance=item)
    return render(request, 'Admin/login/blog.html', {'form': form})


@login_required()
def delete_event(request,pk):

    item = blogpost.objects.get(pk=pk)
    item.delete()

    return redirect('admingallery')


@login_required()
def update_event(request, pk):
    item = get_object_or_404(blogpost, pk=pk)
    if request.method == 'POST':
        form = Blogform(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return redirect('admingallery')
    else:
        form = Blogform(instance=item)
    return render(request, 'Admin/login/blog.html', {'form': form})


def donationsite(request):
    event = blogpost.objects.all()
    if event.exists():
        return render(request,'donations.html')

    else:

        return redirect('index')

@login_required()
def create_event(request):
    if request.method == 'POST':
        form = Blogform(request.POST, request.FILES)
        if form.is_valid():
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            gallery = blogpost(description=description, image=image)
            gallery.save()
            return redirect('admingallery') 
    else:
        form = blogpost()
    return render(request, 'Admin/login/blog.html', {'form': form})

def about(request):
    return render(request,'about.html')

def actionplan(request):
    return render(request,'actionplan.html')