from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm


class SignUpView(CreateView):
    form_class=SignUpForm
    success_url=reverse_lazy('login')
    template_name='registration/signup.html'


def logout_user(request):
    logout(request)
    return redirect("home")



