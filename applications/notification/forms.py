from django import forms

from .models import Notification
from applications.user.models import School

class PreviewNotificationForm(forms.Form):

    CHOICES = map(
        lambda school:
            (school.id, school.name), School.objects.all()
    )


    tittleNotification = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control'
    }),max_length=50, label='Titulo de la notificación:')
    bodyNotification = forms.CharField(widget= forms.TextInput(attrs={
        'class' : 'form-control'
    }),max_length=200, label='Descripción de la Notificación:')
  
class NotificationDataForm (forms.ModelForm):

    class Meta:
        
        model = Notification
        fields = ('__all__')
        widgets = {
            'tittle' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'body' : forms.Textarea(attrs={
                'class' : 'form-control',
                'rows' : 3
            }),
            'icon' : forms.FileInput(attrs={
                'class' : 'form-control'
            }),
            'admin' : forms.Select(attrs={
                'class' : 'form-control'
            }),
            'schools' : forms.SelectMultiple(attrs={
                'class' : 'form-control'
            })
        }
        labels = {
            'tittle' : 'Titulo:',
            'body' : 'Descripción:',
            'icon' : 'Portada:',
            'admin' : 'Administrador:',
            'schools' : 'Facultades (Pulsa Ctrl al momento de seleccionar):'
        }