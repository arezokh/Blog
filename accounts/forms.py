from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields=UserCreationForm.Meta.fields + ('age', 'email', 'photo', 'about',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=UserChangeForm.Meta.fields





class SignUpForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    about=forms.CharField(max_length=255)
    profile_image =forms.FileField(required=False)

    class Meta:
        model=CustomUser
        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'about', 'profile_image']
