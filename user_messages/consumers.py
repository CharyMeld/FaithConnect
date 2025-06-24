import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatRoom, Message
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']  # match URL kwarg
        self.room_group_name = f'chat_{self.room_id}'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data['type'] == 'message':
            username = data['username']
            message = data['message']
            user = await database_sync_to_async(User.objects.get)(username=username)
            room = await database_sync_to_async(ChatRoom.objects.get)(id=self.room_id)
            msg = await database_sync_to_async(Message.objects.create)(
                chat_room=room, sender=user, content=message
            )
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                    'timestamp': msg.timestamp.strftime("%H:%M"),
                    'message_id': msg.id,  # <-- add this
                }
            )
        elif data['type'] == 'read':
            message_id = data['message_id']
            user = await database_sync_to_async(User.objects.get)(username=data['username'])
            msg = await database_sync_to_async(Message.objects.get)(id=message_id)
            await database_sync_to_async(msg.read_by.add)(user)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'read_receipt',
                    'message_id': message_id,
                    'username': data['username'],
                }
            )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'message',
            'message': event['message'],
            'username': event['username'],
            'timestamp': event['timestamp'],
            'message_id': event['message_id'],  # <-- add this
        }))

    async def read_receipt(self, event):
        await self.send(text_data=json.dumps({
            'type': 'read',
            'message_id': event['message_id'],
            'username': event['username'],
        }))

