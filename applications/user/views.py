from pyfcm import FCMNotification

from django.views.generic import View
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


from .models import User, School


# Create your views here.

class UserRegister(View):
    
    #TODO hacer la logica get y post del registro

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserRegister, self).dispatch(request, *args, **kwargs)
    

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
        
        return JsonResponse({"estado" : True}) if user[1] else JsonResponse({"estado" : False})


class UserLogin(View): 

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserLogin, self).dispatch(request, *args, **kwargs)

    def get(self, request):

        return HttpResponse('Este es el login')

    def post(self, request):

        user_id = User.objects.filter(dni = request.POST.get('dni'))
        user_pass = User.objects.filter(dni = request.POST.get('password'))

        return True if user_id and user_pass else False

class SchoolsJSON(View):
    
    def get(self, request):

        lista_facultades = []

        for f in School.objects.all():
            lista_facultades.append(model_to_dict(f))

        context = {}    

        context['Facultades'] = lista_facultades

        return JsonResponse(context)




