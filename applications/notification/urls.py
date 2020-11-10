from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views

urlpatterns = [
    path('fcm/', views.NotificationFCM.as_view()),
    
]
