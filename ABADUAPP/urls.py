from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
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
    path('<str:room_name>/<str:username>/',views.room,name='room'),
    path('available_rooms/',views.available_rooms,name='available_rooms'),
    path('del_all_rooms',views.del_all_rooms,name='del_all_rooms'),
    path('about/',views.about,name='about'),
    path('action/',views.actionplan,name='actionplan')
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:

    urlpatterns +=  static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
