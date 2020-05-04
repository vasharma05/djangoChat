from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'chats'


urlpatterns = [
    path('', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('group/<str:group_name>/', views.group, name='room'),
]
