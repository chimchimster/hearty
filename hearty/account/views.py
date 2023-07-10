from .models import User
from .forms import RegisterUserForm

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('account:login')


class LoginUser(LoginView):
    template_name = 'account/login.html'