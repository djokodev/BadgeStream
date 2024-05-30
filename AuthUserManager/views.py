from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import CustomeUser
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from .forms import CustomeUserLoginForm, CustomeUserRegistrationFrom
from django.contrib import messages


class SignUpView(CreateView):
    model = CustomeUser
    template_name = 'AuthUserManager/register.html'
    form_class = CustomeUserRegistrationFrom
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.password = make_password(form.cleaned_data['password1'])
        user.save()
        response = super().form_valid(form)
        messages.success(self.request, 'Votre compte a été créé avec succès !')
        return response


class SignInView(LoginView):
    authentication_form = CustomeUserLoginForm
    template_name = 'AuthUserManager/login.html'


class ProfilView(LoginRequiredMixin, DetailView):
    model = CustomeUser
    template_name = 'AuthUserManager/profil.html'

    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        badges = user.badges.all()
        context['badges'] = badges
        return context
