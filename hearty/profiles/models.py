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
    city = models.ForeignKey('Cities', on_delete=models.SET_NULL, null=True, verbose_name='Город')

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


class Cities(models.Model):
    city = models.CharField(max_length=50, verbose_name='Название города')
    country = models.ForeignKey('Countries', on_delete=models.SET_NULL, null=True, verbose_name='Страна')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.city


class Countries(models.Model):
    country = models.CharField(max_length=50, verbose_name='Название страны')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.country


class Like(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_likes', verbose_name='Отправитель')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_likes', verbose_name='Получатель')

    def __str__(self):
        return f'Лайк {self.receiver} от {self.sender}'

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


class Dislike(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_dislikes', verbose_name='Отправитель')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_dislikes', verbose_name='Получатель')

    def __str__(self):
        return f'Дизлайк {self.receiver} от {self.sender}'

    class Meta:
        verbose_name = 'Дизлайк'
        verbose_name_plural = 'Дизлайки'