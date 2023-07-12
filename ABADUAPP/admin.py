from django.contrib import admin
from .models import Messages,Gallery,blogpost,Admininfo

# Register your models here.
admin.site.register(Messages)
admin.site.register(Gallery)
admin.site.register(blogpost)
admin.site.register(Admininfo)
