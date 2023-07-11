from django.db import models
from account.models import User
from django.urls import reverse

from .utils import get_upload_path


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name='Пользователь')

    GENDER_CHOICES = (
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
    )

    description = models.TextField(verbose_name='Описание профиля')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
    preferences = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Предпочтения')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_absolute_url(self):
        return reverse('profile', args=[self.pk])

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Images(models.Model):
    profile = models.ForeignKey(Profile, related_name='images', on_delete=models.CASCADE, verbose_name='Профиль')
    image = models.ImageField(upload_to=get_upload_path, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'




