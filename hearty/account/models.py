from django.db import models
from django.utils import timezone
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('Укажите почту!')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    password = models.CharField(max_length=128, verbose_name='Пароль')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    phone_number = PhoneField(blank=False, help_text='Номер телефона', verbose_name='Контактный номер телефона')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    is_staff = models.BooleanField(default=False, verbose_name='Администратор')
    date_joined = models.DateTimeField(default=timezone.now(), verbose_name='Время создания аккаунта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    objects = UserManager()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perm(self, app_label):
        return self.is_staff

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунт'

