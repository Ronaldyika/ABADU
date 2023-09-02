from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from . import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',user_views.index,name='index'),

    #admin registration,login info
    path('register/',user_views.RegisterUser,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name = 'Admin/login/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'Admin/login/logout.html'),name='logout'),

    ##thes field deals with reseting the admin password
    #path('password_reset/',auth_views.PasswordResetView.as_view(template_name = 'Email/password_reset.html'),name='password_reset'),
    #path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'Email/password_reset_done.html'),name='password_reset_done'),
    #path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'Email/password_reset_confirm.html'),name='password_reset_confirm'),
    #path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name = 'Email/password_reset_complete.html'),name='password_reset_complete'),

    #main urls

    path('gallery/',user_views.customergallery, name='gallery'),
    path('adminblog/',user_views.adminblog,name='adminblog'),
    path('create_event/',user_views.create_event,name='create_event'),
    path('admingallery/',user_views.admingallery,name='admingallery'),
    path('delete/<int:pk>/',user_views.deletegallery,name='deletegallery'),
    path('delete_event/<int:pk>/',user_views.delete_event,name='delete_event'),
    path('update/<int:pk>/', user_views.updategallery, name='updategallery'),
    path('updateevent/<int:pk>/', user_views.update_event, name='updateevent'),
    path('donation/',user_views.donationsite,name='donation'), 
    path('about/',user_views.about,name='about'),
    path('action/',user_views.actionplan,name='actionplan'),
    path('upcoming/',user_views.upcoming,name='upcoming'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 