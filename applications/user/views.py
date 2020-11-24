from pyfcm import FCMNotification
from .custom import Validate


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
        
        validate = Validate(request.POST.get('dni'),request.POST.get('email'))

        
        
        if(validate.lenghtDNI() and validate.VerifyEmail()):

            if(not validate.checkDNI() and not validate.CheckEmail()):

                user = User.objects.create(
                    name = request.POST.get('name'),
                    last_name = request.POST.get('last_name'),
                    dni = request.POST.get('dni'),
                    email = request.POST.get('email'),
                    password = request.POST.get('password'),
                    token = request.POST.get('token')
                    )

                user.school.set(request.POST.get('school').split(','))
                user.save()
        
                return JsonResponse({'estado' : 'Cuenta creada'})
            
            else: 
                
                return JsonResponse({'estado' : 'Cuenta existente'})

        else:

            return JsonResponse({'estado' : 'Campo de Dni o Email no valido'})

        


class UserLogin(View): 

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserLogin, self).dispatch(request, *args, **kwargs)

    def get(self, request):

        return HttpResponse('Este es el login')

    def post(self, request):

        userDNI = User.objects.filter(dni = request.POST.get('dni'))
        userPass = User.objects.filter(password = request.POST.get('password'))

        return True if userDNI and userPass else False

class SchoolsJSON(View):
    
    def get(self, request):

        return JsonResponse({'facultades' : [model_to_dict(s) for s in School.objects.all()]})




