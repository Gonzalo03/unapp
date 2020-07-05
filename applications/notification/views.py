from pyfcm import FCMNotification

from  rest_framework import viewsets

from .models import Notification, Notice
from .serializers import NoticeSerializer


# Create your views here.

class NoticeViewset(viewsets.ModelViewSet):

    serializer_class = NoticeSerializer

    queryset = Notice.objects.all()

