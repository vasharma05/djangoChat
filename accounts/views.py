from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView,TemplateView, FormView
from . import forms
# Create your views here.

class Register(CreateView):
    template_name= "register.html"
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    