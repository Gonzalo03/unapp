from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views


urlpatterns = [
    path('school/', views.SchoolsJSON.as_view()),
    path('add/user/', views.UserRegister.as_view())
]
