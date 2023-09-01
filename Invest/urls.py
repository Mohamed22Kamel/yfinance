from django.urls import path
from . import views
urlpatterns = [
    path("", views.home , name='invest-home'),
    path("join", views.join , name='join'),
    path("home/",views.homePage , name='homePage'),
    path('join/login',views.login_page , name='login_page'),
    path('reset/',views.reset_page, name ='reset'),
    path('done',views.done , name='done'),
    path('edit' , views.edit , name='edit'),
    path('delete' , views.delete , name='delete'),
    path('learn', views.learn , name='learn' ),
    path('chat', views.chat , name='chat' )

]
