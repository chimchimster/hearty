import re

from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import User
from .forms import RegisterUserForm, ChangeEmailForm, ChangePasswordForm

from django.urls import reverse_lazy, reverse
from django.views.generic import View, CreateView, DetailView
from django.contrib.auth.views import LoginView


class AccountDetailView(DetailView):
    model = User
    template_name = 'account/detail.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['email_change'] = ChangeEmailForm
        context['password_change'] = ChangePasswordForm

        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('account:login')


class LoginUser(LoginView):
    template_name = 'account/login.html'


class ChangeEmailView(View):
    form = ChangeEmailForm

    def post(self, request, *args, **kwargs):

        email1 = self.request.POST.get('email1')
        email2 = self.request.POST.get('email2')
        password1 = self.request.POST.get('password1')
        password2 = self.request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Введенные пароли не совпадают!')
            return HttpResponseRedirect(reverse('account:account-detail', args=[self.request.user.pk]))

        if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_\-+=])[A-Za-z\d!@#$%^&*()_\-+=]{8,}$', password1):
            messages.error(request, 'Длина пароля должна быть минимум 8 символом. Пароль должен содержать как миминимум 1 цифру, 1 букву в заглавном регистре, 1 специальный символ!')
            return HttpResponseRedirect(reverse('account:account-detail', args=[self.request.user.pk]))

        if email1 != email2:
            messages.error(request, 'Введенные почты не совпадают!')
            return HttpResponseRedirect(reverse('account:account-detail', args=[self.request.user.pk]))

        user = User.objects.get(pk=self.request.user.pk)

        if user.email == email1:
            messages.error(request, 'Введенная почта уже связана с вашим аккаунтом!')
            return HttpResponseRedirect(reverse('account:account-detail', args=[self.request.user.pk]))

        user.email = email1
        user.save()

        messages.info(request, 'Вы успешно сменили почту!')
        return HttpResponseRedirect(reverse('account:account-detail', args=[self.request.user.pk]))


class ChangePasswordView(View):
    form = ChangePasswordForm

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.pk)

        old_password = self.request.POST.get('old_password')
        password1 = self.request.POST.get('password1')
        password2 = self.request.POST.get('password2')

        if not user.check_password(old_password):
            messages.error(request, 'Вы ввели неверный пароль')
            return HttpResponseRedirect(reverse('account:account-detail', args=[self.request.user.pk]))

        if password1 != password2:
            messages.error(request, 'Введенные пароли не совпадают!')
            return HttpResponseRedirect(reverse('account:account-detail', args=[self.request.user.pk]))

        if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_\-+=])[A-Za-z\d!@#$%^&*()_\-+=]{8,}$', password1):
            messages.error(request, 'Длина пароля должна быть минимум 8 символом. Пароль должен содержать как миминимум 1 цифру, 1 букву в заглавном регистре, 1 специальный символ!')
            return HttpResponseRedirect(reverse('account:account-detail', args=[self.request.user.pk]))

        user.set_password(password1)
        user.save()
        messages.info(request, 'Вы успешно изменили пароль!')
        return HttpResponseRedirect(reverse('account:account-detail', args=[self.request.user.pk]))

