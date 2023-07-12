from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.index, name='base'),
    path('signin/',views.signinadmin,name='signin'),
    path('register/',views.registeradmin,name='register'),
    path('gallery/',views.customergallery, name='gallery'),
    path('adminblog/',views.adminblog,name='adminblog'),
    path('admingallery/',views.admingallery,name='admingallery'),
    path('delete/<int:pk>/',views.deletegallery,name='deletegallery'),
    path('update/<int:pk>/', views.updategallery, name='updategallery'),
    path('updateevent/<int:pk>/', views.updategallery, name='updateevent'),
]

if settings.DEBUG:

    urlpatterns +=  static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)