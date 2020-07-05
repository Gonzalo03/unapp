from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views


urlpatterns = [
    path('fcm/', views.NotificationFCM.as_view()),
    path('filter/user/<token>', views.UserFilter.as_view()),
    path('school/', views.SchoolsJSON.as_view()),
    path('add/user/', views.UserRegister.as_view())
]
