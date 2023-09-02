from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Gallery,blogpost


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class Galleryform(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'

class Blogform(forms.ModelForm):
    class Meta:
        model = blogpost
        fields = '__all__'