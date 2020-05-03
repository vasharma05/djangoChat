from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
@login_required
def index(request):
    list_users = User.objects.all()
    return render(request, 'chat/index.html', {'users': list_users})

@login_required
def room(request, room_name):
    users = User.objects.all()
    return render(request, 'chat/room.html', {
        'room_name': room_name, "users": users
    })

@login_required
def group(request, group_name):
    return render(request, 'chat/group.html', {
        'group_name': group_name,
    })