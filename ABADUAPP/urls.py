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
    path('create_event/',views.create_event,name='create_event'),
    path('admingallery/',views.admingallery,name='admingallery'),
    path('delete/<int:pk>/',views.deletegallery,name='deletegallery'),
    path('delete_event/<int:pk>/',views.delete_event,name='delete_event'),
    path('update/<int:pk>/', views.updategallery, name='updategallery'),
    path('updateevent/<int:pk>/', views.update_event, name='updateevent'),
    path('donation/',views.donationsite,name='donation'), 
    path('chatroom',views.HomePage,name='home'),
    path('<str:room_name>/<str:username>/',views.messageview,name='room'),
]

if settings.DEBUG:

    urlpatterns +=  static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)