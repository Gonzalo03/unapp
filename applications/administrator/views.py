from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


from .forms import AdminLoginForm
from .models import Admin

import secrets


SECRET_TOKEN_ADMIN = secrets.token_hex(16)

class AdminLogin(FormView):

    form_class = AdminLoginForm

    template_name = 'admin/login.html'

    def form_valid(self, form):

        email = form.cleaned_data['adminEmail']
        pawd = form.cleaned_data['adminPass']

        for a in Admin.objects.all():

            if  (a.email == email) and (a.password == pawd):
                
                return HttpResponseRedirect(reverse('notificationApp:notification', args=('{}'.format(SECRET_TOKEN_ADMIN),), kwargs={}))

            else:

                return HttpResponseRedirect(reverse('notificationApp:notification', args=('denied',), kwargs={}))
