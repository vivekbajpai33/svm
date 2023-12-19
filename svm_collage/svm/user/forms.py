from django import forms 
from captcha.fields import CaptchaField 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import *
# from captcha.widgets import ReCaptchaV2Checkbox 
  
  
class ContactForm(forms.Form): 
    captcha = CaptchaField() 

class MediaForm(forms.ModelForm):    
    class Meta:
        model  = StudentSocialMedia
        fields = "__all__"

class EditUserProfile(UserChangeForm):
    password = None
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','type':'email'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    class Meta:
        model = User
        fields = ('email','username','first_name','last_name')
    

class PasswordReset(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2 = forms.CharField(min_length=8 , widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
                                    

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')




