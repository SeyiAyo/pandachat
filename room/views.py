from django.shortcuts import render
from .models import Message
from django.contrib.auth.decorators import login_required

from .models import Room

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, room_name):
    room = Room.objects.get(slug=room_name)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    
    return render(request, 'room/chatwindow.html', {'room': room, 'messages': messages})