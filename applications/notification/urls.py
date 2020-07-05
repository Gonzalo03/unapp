from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('api/notice', views.NoticeViewset)


urlpatterns = [
    path('', include(router.urls)),
    
]
