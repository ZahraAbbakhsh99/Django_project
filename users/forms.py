from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
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


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        email = self.cleaned_data["email"]

        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")

        if password != confirm_password:
            raise ValidationError("Password and confirmation are not the same.")
