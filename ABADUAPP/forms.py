from django import forms
from .models import Gallery,blogpost


class Galleryform(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'

class Blogform(forms.ModelForm):
    class Meta:
        model = blogpost
        fields = '__all__'