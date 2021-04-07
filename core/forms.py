from django.forms import ModelForm 
from .models import Order
from django import forms

from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class OrderForm(ModelForm):
    
    class Meta:
        model = Order
        fields = "__all__"


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User 
        fields=['email','username','password1','password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        for instance in User.objects.all():
            if instance.email == email:
                raise forms.ValidationError('This email already in use')



    def clean_username(self):
        username = self.cleaned_data.get('username')
        for instance in User.objects.all():
            if instance.username == username:
                raise forms.ValidationError('username is in Use')
        return username        
    
