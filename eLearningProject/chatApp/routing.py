from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path('ws/chatApp/<str:room_name>)/', consumers.ChatConsumer),
]