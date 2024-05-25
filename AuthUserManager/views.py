from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .models import CustomeUser
from django.urls import reverse_lazy
from .forms import CustomeUserLoginForm, CustomeUserRegistrationFrom
from django.contrib import messages

class SignUpView(CreateView):
    model = CustomeUser
    template_name = 'AuthUserManager/register.html'
    form_class = CustomeUserRegistrationFrom
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Votre compte a été créé avec succès !')
        return response


class SignInView(LoginView):
    authentication_form = CustomeUserLoginForm
    template_name = 'AuthUserManager/login.html'
