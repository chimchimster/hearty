from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Like, Notification


@receiver(post_save, sender=Like.sender)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        print(instance)
        sender_profile = instance.sender

        receiver_profile = instance.receiver

        notification_message = f"Вы понравились {sender_profile}!"

        Notification.objects.create(user=receiver_profile.user, message=notification_message)