from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from django.urls import reverse


from .forms import PreviewNotificationForm, NotificationDataForm
from .models import Notification, User
from applications.administrator.views import SECRET_TOKEN_ADMIN

from pyfcm import FCMNotification
from datetime import datetime
import json






# Create your views here.

class NotificationFCM(View):

    
    def get(self, request, *args, **kwargs):

        print(self.kwargs)

        if self.kwargs['url'] == SECRET_TOKEN_ADMIN:
            
            return render(request, 'notification/noti.html', {
                'Notification' : Notification.objects.all(), 
                'formPreview' : PreviewNotificationForm,
                'formData' : NotificationDataForm})
        else:

            return HttpResponse('ya salio la csmr')

    def post(self, request, *args, **kwargs):

        formData = NotificationDataForm(request.POST, request.FILES)

        if formData.is_valid():

            formInstance = formData.save()
            userTokenKist = [u.token for u in User.objects.filter(school__in= request.POST.getlist('schools')).distinct()]

            FCM_API_KEY = 'AAAA9Ko7Kvw:APA91bFQXYNGsPfXaNx8akVvZVfEJrTw_ZUB_DPmXkWmL-YY0MVRPrvchpqyoQphhzSpHz39Z8pH-7yUlCniIvvU8pU7sLrcN3a2BHsWR-UXlS0CotrFS-vLy95YLOfebUo_w0AAHLHO'

            data = {
                "tittle" : formInstance.tittle,
                "body" : formInstance.body,
                "image-url": formInstance.icon.url,
                "created_at" :str(formInstance.created),
                "click_action" : "FLUTTER_NOTIFICATION_CLICK"
                }

            push_service = FCMNotification(
                api_key= FCM_API_KEY
                )

            r = push_service.notify_multiple_devices(
                registration_ids= userTokenKist,
                message_title = request.POST.get('tittleNotification'),
                message_body= request.POST.get('bodyNotification'),
                data_message= json.dump(data)
                )
            print(r)
            return  HttpResponseRedirect(reverse('notificationApp:notification', args=('access',), kwargs={})) if r else HttpResponse('Push fallido')
        else:

            return HttpResponse('inconcluido')
        
class NotificationJSON(View):

    def get(request, *args, **kwargs):
        
        listaNotificaciones = []

        for n in Notification.objects.all():

            listaNotificaciones.append({
                'titulo' : n.tittle,
                'cuerpo' : n.body,
                'creado' : str(n.created)
            })

        return JsonResponse({'Notificaciones' : listaNotificaciones})