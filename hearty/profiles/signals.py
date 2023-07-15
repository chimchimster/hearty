from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import User

@receiver(post_save, sender=User)
def get_like(sender, instance, liked, **kwargs):
    if liked:
        pass