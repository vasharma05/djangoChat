import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from . import models
from django.contrib.auth.models import User
class ChatConsumer(WebsocketConsumer):
    def create_room(self):
        self.room = models.Room.objects.create(name=str(self.room_name))
        print(self.room)
        self.room.users.add(self.user,self.room_user)
        print(self.room.users.all())

    def check_room(self):
        self.username = self.scope['user'].username
        self.user = User.objects.get(username=self.username)
        self.room_user = User.objects.get(username=self.room_name)
        print(self.user, self.room_user)
        room_list = models.Room.objects.filter(users = self.user)
        self.room_id = None
        for room in room_list:
            print(room.users.all())
            if self.room_user in room.users.all():
                self.room_id = room.id
                self.room = room
                break
        if self.room_id is None:
            print('Stuck')
            self.create_room()
            
            # self.room_id = self.room.id
        print(self.room)


    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = '%s' % self.room_name
        
        # print(room_list)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        self.check_room()
        print(self.room_id)

    def fetch_messages(self, data):
        messages = self.room.getMessages()
        result = []
        for message in messages:
            result.append({
                "author": message.author.username,
                'content': message.content,
                'timestamp': str(message.timestamp)
            })
        data = {
            'command': 'messages',
            "messages": result
        }
        # print(data)
        self.send(text_data=json.dumps(data))
        

    def new_message(self, data):
        if (data["message"]["author"] == self.user.username):
            author = self.user
        else:
            author = self.room_user
        message = models.Message.objects.create(
            author= author,
            content= data['message']['content']
        )
        self.room.message_set.add(message)
        print(data)
        self.send_chat_message(data)

    commands = {
        "fetch_messages": fetch_messages,
        "new_message": new_message
    }

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)
    
    def send_chat_message(self,message):
        # Send message to room group
        self.send(text_data=json.dumps(message))
        async_to_sync(self.channel_layer.group_send)(
            self.username,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))