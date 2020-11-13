from pyfcm import FCMNotification

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from  rest_framework import viewsets

from applications.user.models import School
from .models import Notification
from .serializers import NoticeSerializer


# Create your views here.

class NotificationFCM(View):

    def get(self, request):

        print(request.GET.get('fac'), request.GET.get('titulo'), request.GET.get('contenido'))
        

        return render(request, 'notification/noti.html', {'school' : School.objects.all()})











        '''
        push_service = FCMNotification(api_key='AAAA9Ko7Kvw:APA91bFQXYNGsPfXaNx8akVvZVfEJrTw_ZUB_DPmXkWmL-YY0MVRPrvchpqyoQphhzSpHz39Z8pH-7yUlCniIvvU8pU7sLrcN3a2BHsWR-UXlS0CotrFS-vLy95YLOfebUo_w0AAHLHO')
        
        r = push_service.notify_single_device(
            registration_id='ebIRglShjCY:APA91bEBDttXRN9-oK6HjcmK9elgQJt1U9Wf6NCU2DbpY4xhTuFzJoilPzDhAcivWovA7feoNh8_cBpnkRRlbCFjPPdgZ6M9-ZFGTNKDmAHMmIoEsZ41zpr3e6GnqpJTyMmOkRypMwat',
            message_title= 'hola papi',
            message_body= 'xD',
        )
         
        print(r)

        return HttpResponse('push concluido') if r else HttpResponse('Push fallido')

        '''
