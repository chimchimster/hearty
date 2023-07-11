from django import forms
from .models import User
from datetime import datetime


class RegisterUserForm(forms.ModelForm):

    start_year = datetime.today().year - 18

    BIRTH_YEAR_CHOICES = range(1950, start_year)

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)
    bdate = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

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




