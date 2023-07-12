from django import forms
from .models import User
from phone_field import PhoneField
from datetime import datetime


class RegisterUserForm(forms.ModelForm):

    start_year = datetime.today().year - 18

    BIRTH_YEAR_CHOICES = range(1950, start_year)

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    bdate = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли должны совпадать!')
        return cd['password2']


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-input'})
        }


class ChangeEmailForm(forms.Form):
    email1 = forms.CharField(label='Новая почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    email2 = forms.CharField(label='Подтверждение новой почты', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Подтверждение нового пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
