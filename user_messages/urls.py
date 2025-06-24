from django.urls import path
from . import views

app_name = 'user_messages'

urlpatterns = [
    path('', views.messages_home, name='messages_home'),  # main landing page
    path('chats/', views.chat_list, name='chat_list'),    # list of all chats
    path('send_message/', views.send_message, name='send_message'),
    path('chat/<int:room_id>/', views.chat_room, name='chat_room'),
    path('create_group/', views.create_group, name='create_group'),
    path('start-one-on-one/', views.start_one_on_one, name='start_one_on_one'),
]

