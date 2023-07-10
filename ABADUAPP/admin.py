from django.contrib import admin
from .models import Customer,Messages,Gallery,blog

# Register your models here.
admin.site.register(Customer)
admin.site.register(Messages)
admin.site.register(Gallery)
admin.site.register(blog)
