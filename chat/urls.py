from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "chat"
urlpatterns = [
    path('', TemplateView.as_view(template_name='chat/home.html'), name='home'),
    path('chat/', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
]