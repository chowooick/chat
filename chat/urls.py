from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('chat/<int:room_name>/', views.room, name='room'),
]