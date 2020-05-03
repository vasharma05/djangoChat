from django.urls import path

from . import views

app_name = 'chats'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('group/<str:group_name>/', views.group, name='room'),

]
