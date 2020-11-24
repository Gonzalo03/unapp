from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from django.urls import reverse_lazy

from .forms import PreviewNotificationForm, NotificationDataForm
from .models import Notification, User

from pyfcm import FCMNotification




# Create your views here.

class NotificationFCM(View):
    
    def get(self, request):

        return render(request, 'notification/noti.html', {
            'Notification' : Notification.objects.all(), 
            'formPreview' : PreviewNotificationForm,
            'formData' : NotificationDataForm})

    def post(self, request):

        print(request.POST)

        formData = NotificationDataForm(request.POST, request.FILES)

        if formData.is_valid():
            formData.save()
            data = {
                'tittle' : request.POST.get('tittle'),
                'body' : request.POST.get('body'),
                'image-url' : Notification.objects.get(tittle=request.POST.get('tittle')).icon.url,
                'click_action' : 'FLUTTER_NOTIFICATION_CLICK'
                }

            push_service = FCMNotification(
                api_key='AAAA9Ko7Kvw:APA91bFQXYNGsPfXaNx8akVvZVfEJrTw_ZUB_DPmXkWmL-YY0MVRPrvchpqyoQphhzSpHz39Z8pH-7yUlCniIvvU8pU7sLrcN3a2BHsWR-UXlS0CotrFS-vLy95YLOfebUo_w0AAHLHO'
                )

            r = push_service.notify_multiple_devices(
                registration_ids= [u.token for u in User.objects.filter(school__in= request.POST.getlist('schools'))],
                message_title = request.POST.get('tittle'),
                message_body= request.POST.get('body'),
                data_message= data
                )
            print(r)
            return  HttpResponseRedirect(reverse_lazy('notificactionApp:notification')) if r else HttpResponse('Push fallido')
        else:

            return HttpResponse('inconcluido')
        
