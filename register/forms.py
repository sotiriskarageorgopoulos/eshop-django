from django import forms
from django.forms import fields, widgets
from register.models import UserModel

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['name','surname','email','password','street','postal_code','city','province','tel']
        widgets = {
            'password': forms.PasswordInput()
        }
    
    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class'] = "register-form-fields"
        self.fields['surname'].widget.attrs['class'] = "register-form-fields"
        self.fields['email'].widget.attrs['class'] = "register-form-fields"
        self.fields['password'].widget.attrs['class'] = "register-form-fields"
        self.fields['street'].widget.attrs['class'] = "register-form-fields"
        self.fields['postal_code'].widget.attrs['class'] = "register-form-fields"
        self.fields['city'].widget.attrs['class'] = "register-form-fields"
        self.fields['province'].widget.attrs['class'] = "register-form-fields"
        self.fields['tel'].widget.attrs['class'] = "register-form-fields"