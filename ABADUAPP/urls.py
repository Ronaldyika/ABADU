from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.index, name='base'),
    path('signin/',views.signinadmin,name='signin'),
    path('regcustomer/',views.registercustomer,name='regcustomer'),
    path('login/',views.logincustomer,name='login'),
    path('register/',views.registeradmin,name='register'),
    path('gallery/',views.customergallery, name='gallery')
]

if settings.DEBUG:

    urlpatterns +=  static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)