from django.urls import path
from . import views
from . import routing

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('room/<slug:room_name>/', views.room, name='room'),
]

websocket_urlpatterns = routing.websocket_urlpatterns