from django.urls import path
from youtube.consumers import *

websocket_urlpatterns = [
    path(r'videos/<str:room_name>/', ChatConsumer),
]
