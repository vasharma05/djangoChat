from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=256, default='check', unique=False)
    group = models.BooleanField()
    users = models.ManyToManyField(User)
    
    def __str__(self):
        return str(self.id)
    
    def getMessages(self):
        return self.message_set.all()

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


    def __str__(self):
        return self.content
    