from django.contrib.auth.models import User
from chats.models import Room, Message
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name="api:user-detail", read_only=True)
    # room = RoomSerializer(read_only=True)
    class Meta:
        model = Message
        fields = [ 'author', 'content',]

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    message_set = MessageSerializer(many=True)
    class Meta:
        model = Room
        fields = ['name', 'group', 'users', 'message_set']

