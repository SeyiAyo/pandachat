from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Room

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})