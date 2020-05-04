from django.urls import path, include
from . import views
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'rooms',views.RoomViewSet)
router.register(r'messages', views.MessageViewSet)
app_name= 'api'

urlpatterns = [
    path('', include(router.urls)),
]