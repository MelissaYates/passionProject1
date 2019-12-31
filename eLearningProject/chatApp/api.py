from rest_framework import viewsets
# from .models import UserProfile, Message
# from .serializers import UserSerializer, MessageSerializer
from .serializers import UsersSerializer,ChatSerializer
from .models import Users, Chat

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserSerializer
#
#
# class MessageViewSet(viewsets.ModelViewSet):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    