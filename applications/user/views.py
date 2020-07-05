from pyfcm import FCMNotification
import requests

from django.views.generic import View
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.db.models import QuerySet

from  rest_framework import viewsets 
from rest_framework.generics import ListAPIView


from .models import User, School
from .serializers import UserSerializer, SchoolSerializer


# Create your views here.

class UserFilter(ListAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(
            token = self.kwargs.get('token', '')
        )


class UserRegister(View):
    
    #TODO hacer la logica get y post del registro
    def get(self, request):

            return HttpResponse('Aqui es el registro de usuarios')

    def post(self, request):

        user = User.objects.get_or_create(
            name = request.POST.get('name'),
            last_name = request.POST.get('last_name'),
            dni = request.POST.get('dni'),
            email = request.POST.get('email'),
            password = request.POST.get('password'),
            token = request.POST.get('token')
        )

        user[0].school.set(request.POST.get('school').split(','))
        user[0].save()
        
        return HttpResponse('Registro correcto') if user[1] else HttpResponse('Cuenta existente')

class SchoolsJSON(View):
    
    def get(self, request):

        lista_facultades = []

        for f in School.objects.all():
            lista_facultades.append(model_to_dict(f))

        context = {}    

        context['Facultades'] = lista_facultades

        return JsonResponse(context)


class NotificationFCM(View):

    def get(self, request):

        request = requests.get('http://goxx.pythonanywhere.com/api/notification/?format=json')

        push_service = FCMNotification(api_key='AAAA9Ko7Kvw:APA91bFQXYNGsPfXaNx8akVvZVfEJrTw_ZUB_DPmXkWmL-YY0MVRPrvchpqyoQphhzSpHz39Z8pH-7yUlCniIvvU8pU7sLrcN3a2BHsWR-UXlS0CotrFS-vLy95YLOfebUo_w0AAHLHO')
        
        r = push_service.notify_single_device(
            registration_id='cxTy09o8nV4:APA91bEwBZIZ-aqyS1mJVStZxwNLrYEEFttbUL_cBpUV4WtaqYGNG7xs_xJz4fWN0542tZ3w7aA8c_eZz1iwekzP_MfENgnVBKBMKv0HIT1QO46AhyuOMdXJh2qkC5oM6cJP6S81RnPE',
            message_title= request.json()[0]['tittle'],
            message_body= request.json()[0]['body'],
            message_icon= 'pta'

        )
         
        print(r)

        return HttpResponse('push concluido') if r else HttpResponse('Push fallido')


