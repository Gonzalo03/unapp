from django.urls import path


from . import views


app_name = 'adminApp'

urlpatterns = [
    path('login-administrator/', views.AdminLogin.as_view(), name = 'logAdmin'),
   
    
]

