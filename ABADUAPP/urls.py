from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='base'),
    path('signin/',views.signinadmin,name='signin'),
    path('regcustomer/',views.registercustomer,name='regcustomer'),
    path('login/',views.logincustomer,name='login'),
    path('register/',views.registeradmin,name='register')
]