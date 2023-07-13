from django.contrib import admin
from .models import Message,Gallery,blogpost,Admininfo,Room

# Register your models here.
admin.site.register(Message)
admin.site.register(Gallery)
admin.site.register(Room)
admin.site.register(blogpost)
admin.site.register(Admininfo)
