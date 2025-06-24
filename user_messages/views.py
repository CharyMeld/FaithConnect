from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import ChatRoom, Message

User = get_user_model()  # Correctly get the active User model

@login_required
def messages_home(request):
    rooms = request.user.chatrooms.all()
    return render(request, 'user_messages/messages_home.html', {'rooms': rooms})

@login_required
def send_message(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        content = request.POST.get('content')
        file = request.FILES.get('file')
        room = get_object_or_404(ChatRoom, id=room_id)

        receiver = None
        if not room.is_group:
            receiver = room.participants.exclude(id=request.user.id).first()

        Message.objects.create(
            chat_room=room,
            sender=request.user,
            receiver=receiver,
            content=content,
            file=file
        )

        return redirect('user_messages:chat_room', room_id=room.id)

@login_required
def chat_list(request):
    rooms = request.user.chatrooms.all()
    return render(request, 'user_messages/chat_list.html', {'rooms': rooms})

@login_required
def chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    if request.user not in room.participants.all():
        return redirect('user_messages:chat_list')
    messages = room.messages.order_by('timestamp')
    return render(request, 'user_messages/chat_room.html', {'room': room, 'messages': messages})

@login_required
def create_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        participants = request.POST.getlist('participants')  # list of user IDs
        room = ChatRoom.objects.create(name=name, is_group=True, created_by=request.user)
        room.participants.add(request.user, *participants)
        return redirect('user_messages:chat_room', room_id=room.id)

    users = User.objects.exclude(id=request.user.id)
    return render(request, 'user_messages/create_group.html', {'users': users})

@login_required
def start_one_on_one(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        other_user = get_object_or_404(User, id=user_id)

        existing_room = ChatRoom.objects.filter(
            is_group=False,
            participants=request.user
        ).filter(participants=other_user).first()

        if existing_room:
            return redirect('user_messages:chat_room', room_id=existing_room.id)
        else:
            room = ChatRoom.objects.create(is_group=False, created_by=request.user)
            room.participants.add(request.user, other_user)
            return redirect('user_messages:chat_room', room_id=room.id)

    users = User.objects.exclude(id=request.user.id)
    return render(request, 'user_messages/start_one_on_one.html', {'users': users})

