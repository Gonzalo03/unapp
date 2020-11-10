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
        
        return HttpResponse('Registro correcto') if user[1] else HttpResponse('Cuenta existente')


class UserLogin(View): 

    def get(self, request):
        return HttpResponse('Este es el login')
    

class SchoolsJSON(View):
    
    def get(self, request):

        lista_facultades = []

        for f in School.objects.all():
            lista_facultades.append(model_to_dict(f))

        context = {}    

        context['Facultades'] = lista_facultades

        return JsonResponse(context)




