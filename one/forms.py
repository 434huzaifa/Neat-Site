from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from django.core.exceptions import ValidationError

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
        return self.cleaned_data


class CreateSalon(forms.ModelForm):
    sal_phn_no = forms.CharField(max_length=13,min_length=11,widget=forms.NumberInput())
    sal_ctime = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))
    sal_otime = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))
    sal_about=forms.CharField()
    

    class Meta:
        model = models.salon
        fields = ['sal_name', 'sal_phn_no', 'sal_adr', 'sal_otime', 'sal_ctime', 'type', 'sal_about']
        
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sal_name'].required = True
        self.fields['sal_phn_no'].required = True
        self.fields['sal_adr'].required = True
        self.fields['sal_otime'].required = True
        self.fields['sal_ctime'].required = True
        self.fields['type'].required = True


class CreateCleint(forms.ModelForm):
    cl_phn_no =  forms.CharField(max_length=13,min_length=11,widget=forms.NumberInput())

    class Meta:
        model = models.client
        fields = ['cl_phn_no', 'cl_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cl_phn_no'].required = True
        self.fields['cl_name'].required = True
        
class CreateService(forms.ModelForm):
    s_about=forms.CharField()
    
    class Meta:
        model=models.services
        fields=['s_name','s_price','s_ehour','s_emin','s_about']
        
        def __init__(self,*args,**kwargs):
            super().__init__(*args, **kwargs)
            self.fields['s_name'].required=True
            self.fields['s_price'].required=True
            self.fields['s_ehour'].required=True
            self.fields['s_emin'].required=True
            
class CreateAppointmentForm(forms.ModelForm):
    class Meta:
        model=models.apointment
        fields='__all__'