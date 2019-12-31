from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('chat', views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('api/messages', views.message_list, name='message-list'),
    path('api/users/<int:pk>', views.user_list, name='user-detail'),
    path('api/users', views.user_list, name='user-list'),
    path('logout', LogoutView.as_view(next_page='index'), name='logout'),
    path('register', views.register_view, name='register'),
    # path('view_users/', views.view_users, name='view_users'),
    # path('save_msg/', views.save_msg, name='save_msg'),
    # path('get_chat/', views.get_chat, name='get_chat'),
    # path('view_msg/', views.view_msg, name='view_msg'),

]