from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Room(models.Model):
#     name = models.CharField(max_length= 256)
#     users = models.ManyToManyField(User)



class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room = models.CharField(max_length=256, primary_key=False)
    # room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')

    def __str__(self):
        return self.author.username
    def last_10_messages(room):
        return Message.objects.filter(room=room).order_by("timestamp").all()[:10]

