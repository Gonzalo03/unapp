from django.urls import path
from rest_framework import routers

from . import views

app_name = 'notificactionApp'

urlpatterns = [
    path('fcm/', views.NotificationFCM.as_view(), name = 'notification'),
    
]

