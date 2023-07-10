from django import forms
from .models import User


class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли должны совпадать!')
        return cd['password2']


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']




