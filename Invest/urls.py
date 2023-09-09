from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path("", views.home , name='invest-home'),
    path("join", views.join , name='join'),
    path("dashboard",views.homePage , name='dashboard'),
    path('join/login',views.login_page , name='login_page'),
    path('reset/',views.reset_page, name ='reset'),
    path('done',views.done , name='done'),
    path('edit' , views.edit , name='edit'),
    path('delete' , views.delete , name='delete'),
    path('learn', views.learn , name='learn' ),
    path('chat', views.chat , name='chat' )

]+static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
