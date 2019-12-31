from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Message, UserProfile
from .serializers import MessageSerializer, UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .serializers import UsersSerializer,ChatSerializer
# from .models import Users, Chat
from django.shortcuts import render
import datetime
from django.utils import timezone
from django.db.models import Q


def index(request):
    return render(request, 'chatApp/index.html')


# # @api_view(['POST'])
# def view_users(request):
#     if request.method == 'POST':
#         user, created = Users.objects.update_or_create(
#             user_id=request.data['sender'],
#             defaults={
#                 'last_visit': datetime.datetime.now(tz=timezone.utc)
#             })
#
#         time=datetime.datetime.now(tz=timezone.utc) - datetime.timedelta(seconds=15)
#         data={
#             'status': 'true',
#             'data': UsersSerializer(Users.objects.filter(last_visit__gte=time), many=True).data
#         }
#         return Response(data, status=status.HTTP_200_OK)
#
#
# # @api_view(['POST'])
# def save_msg(request):
#     if request.method == 'POST':
#         time=datetime.datetime.now(tz=timezone.utc)
#         chat = Chat(
#             sender=request.data['sender'],
#             receiver=request.data['receiver'],
#             msg=request.data['msg'],
#             time=time
#         )
#         chat.save();
#         data={
#             'status': 'true'
#         }
#         return Response(data, status=status.HTTP_200_OK)
#
# # @api_view(['POST'])
# def get_chat(request):
#     if request.method == 'POST':
#         time=datetime.datetime.now(tz=timezone.utc)- datetime.timedelta(seconds=150)
#         data={
#             'status': 'true',
#             'data': ChatSerializer(Chat.objects.filter(time__gte=time,receiver=request.data['sender']), many=True).data
#         }
#         return Response(data, status=status.HTTP_200_OK)
#
# # @api_view(['POST'])
# def view_msg(request):
#     if request.method == 'POST':
#         data={
#             'status': 'true',
#             'data': ChatSerializer(Chat.objects.filter(Q(receiver=request.data['sender'],sender=request.data['receiver']) | Q(receiver=request.data['receiver'],sender=request.data['sender'])), many=True).data
#         }
#         return Response(data, status=status.HTTP_200_OK)


def index(request):
    if request.user.is_authenticated:
        return redirect('chats')
    if request.method == 'GET':
        return render(request, 'chatApp/index.html', {})
    if request.method == "POST":
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
        else:
            return HttpResponse('{"error": "User does not exist"}')
        return redirect('chats')


@csrf_exempt
def user_list(request, pk=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        if pk:
            users = User.objects.filter(id=pk)
        else:
            users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user = User.objects.create_user(username=data['username'], password=data['password'])
            UserProfile.objects.create(user=user)
            return JsonResponse(data, status=201)
        except Exception:
            return JsonResponse({'error': "Something went wrong"}, status=400)


@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def register_view(request):
    """
    Render registration template
    """
    if request.user.is_authenticated:
        return redirect('chats')
    return render(request, 'chatApp/register.html', {})


def chat_view(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, 'chatApp/chat.html', {'users': User.objects.exclude(username=request.user.username)})


def message_view(request, sender, receiver):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, "chatApp/messages.html",
                      {'users': User.objects.exclude(username=request.user.username),
                       'receiver': User.objects.get(id=receiver),
                       'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) | Message.objects.filter(sender_id=receiver, receiver_id=sender)})
