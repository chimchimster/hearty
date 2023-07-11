import os

from django.utils import timezone


def get_upload_path(instance, filename):
    email = instance.profile.user.email
    current_date = timezone.now().strftime('%d/%m/%Y')
    base_path = f'media/{email}/{current_date}'

    return os.path.join(base_path, filename)

