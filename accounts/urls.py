from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name="accounts"

urlpatterns = [
    path("register/", views.Register.as_view(), name='register'),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]