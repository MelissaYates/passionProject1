
from django.contrib.auth.models import User
from rest_framework import serializers
# from .models import Chat, Users
from .models import Message


# class UsersSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Users
#         fields = ('user_id', 'last_visit')
#
#
# class ChatSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Chat
#         fields = ('sender', 'receiver','msg','time')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    online = serializers.ReadOnlyField(source='userprofile.online')

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'online']


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']