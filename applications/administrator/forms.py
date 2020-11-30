from django import forms


class AdminLoginForm(forms.Form):

    adminEmail = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'form-control',
    }))

    adminPass = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control'
    }))

    