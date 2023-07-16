from djongo import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name='Chats', verbose_name='Чат')

    def __str__(self):
        return f'Чат {self.pk}'

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages', verbose_name='Чат')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Отправитель')
    context = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время сообщения')

    def __str__(self):
        return f'Сообщение {self.pk} от пользователя {self.sender.email} в чате {self.chat}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'