from django import forms
from django.contrib.auth.models import User
from .models import *


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'from_control'}),
            'last_name': forms.TextInput(attrs={'class': 'from_control'}),
            'email': forms.EmailInput(attrs={'class': 'from_control'}),
        }
        labels ={
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email'
        }
