from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class Registerform(UserCreationForm):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email=forms.EmailField()
    
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image','location','occupation','monthly_income']      

"""class PasswordUpdateForm(PasswordChangeForm):
    class Meta:
        model=User
        fields=['password1']    """      