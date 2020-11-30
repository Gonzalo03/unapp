from django.urls import path
from rest_framework import routers

from . import views

app_name = 'notificationApp'

urlpatterns = [
    path('fcm/<url>/', views.NotificationFCM.as_view(), name = 'notification'),
    path('notifications/', views.NotificationJSON.as_view())
]

