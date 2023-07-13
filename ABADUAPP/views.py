from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import blogpost,Message,Gallery,Admininfo,Room
from .forms import Galleryform,Blogform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,'main/index.html')

def registeradmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            try:
                user = Admininfo.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Your account has been created successfully!')
                return redirect('signin')
            except:
                messages.error(request, 'An error occurred while creating your account. Please try again.')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')
    return render(request, 'adminsite/register.html')


def signinadmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admingallery')
        else:
            messages.error(request, 'Invalid Username or password')
    return render(request, 'adminsite/login.html')

def customergallery(request):
    cards = blogpost.objects.all()
    posts = Gallery.objects.all()
    context = {
        'posts':posts,
        'cards':cards
    }

    return render(request,'customer/gallery.html',context)

def admingallery(request):
    cards = blogpost.objects.all()
    posts = Gallery.objects.all()
    context = {
        'posts':posts,
        'cards':cards
    }
    
    return render(request, 'adminsite/gallery.html', context)

def adminblog(request):
    if request.method == 'POST':
        form = Galleryform(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            gallery = Gallery(title=title, description=description, image=image)
            gallery.save()
            return redirect('admingallery')  # Redirect to the gallery page after successful form submission
    else:
        form = Galleryform()
    return render(request, 'adminsite/blog.html', {'form': form})

def deletegallery(request,pk):

    item = Gallery.objects.get(pk=pk)
    item.delete()

    return redirect('admingallery')

def updategallery(request,pk):
    item = get_object_or_404(Gallery, pk=pk)
    if request.method == 'POST':
        form = Galleryform(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('admingallery')
    else:
        form = Galleryform(instance=item)
    return render(request, 'adminsite/blog.html', {'form': form})


def delete_event(request,pk):

    item = blogpost.objects.get(pk=pk)
    item.delete()

    return redirect('admingallery')


def update_event(request,pk):
    item = get_object_or_404(blogpost,pk=pk)
    if request.method == 'POST':
        form = Blogform(request.POST, request.FILES, instance=item)
        
        if form.is_valid():
            form.save()
            return redirect('admingallery')
    else:
        form = Blogform(instance=item)
    return render(request, 'adminsite/blog.html', {'form': form})


def donationsite(request):
    event = blogpost.objects.all()
    if event.exists():
        return render(request,'base/donation.html')

    else:

        return redirect('base')

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
    return render(request, 'adminsite/blog.html', {'form': form})

#this section deals with the chat section

def HomePage(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']

        try:
            get_room = Room.objects.get(room_name=room)
            return redirect('room', room_name=room, username=username)
        
        except Room.DoesNotExist:
            new_room = Room(room_name = room)
            new_room.save()
            return redirect('room',room_name=room,username=username)    
    return render(request, 'chat/index.html')

def messageview(request,room_name,username):
    get_room = Room.objects.get(room_name=room_name)
    if request.method =='POST':
        message = request.POST['message']

        new_message = Message(room=get_room,sender=username,message=message)
        new_message.save()

    get_messages = Message.objects.filter(room=get_room)

    context = {
        'messages':get_messages,
        'user':username
    }

    return render(request,'chat/message.html',context)
