from django.shortcuts import render, redirect, HttpResponseRedirect
from admin_corporate.forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserPasswordChangeForm, UserSetPasswordForm
from django.views.generic import CreateView
from django.contrib.auth import logout, views as auth_views
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def dashboard(request):
    context = {
        'segment': 'dashboard'
    }
    return render(request, 'pages/dashboard.html', context)

@login_required(login_url='/accounts/login/')
def tables(request):
    context = {
        'segment': 'tables'
    }
    return render(request, 'pages/tables.html', context)

@login_required(login_url='/accounts/login/')
def wallet(request):
    context = {
        'segment': 'wallet'
    }
    return render(request, 'pages/wallet.html', context)

@login_required(login_url='/accounts/login/')
def rtl(request):
    context = {
        'segment': 'rtl'
    }
    return render(request, 'pages/rtl.html', context)

@login_required(login_url='/accounts/login/')
def profile(request):
    context = {
        'segment': 'profile'
    }
    return render(request, 'pages/profile.html', context)

class UserRegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/sign-up.html'
    success_url = '/accounts/login/'

    def get_context_data(self, *args, **kwargs):
        context = super(UserRegistrationView, self).get_context_data(*args, **kwargs)
        context['segment'] = 'register'
        return context

class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/sign-in.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserLoginView, self).get_context_data(*args, **kwargs)
        context['segment'] = 'login'
        return context

class UserPasswordResetView(auth_views.PasswordResetView):
  template_name = 'accounts/password-reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/password-reset-confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(auth_views.PasswordChangeView):
  template_name = 'accounts/password-change.html'
  form_class = UserPasswordChangeForm

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))