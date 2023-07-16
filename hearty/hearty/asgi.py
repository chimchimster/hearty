"""
ASGI config for hearty project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hearty.settings')

django_application = get_asgi_application()
static_handler = ASGIStaticFilesHandler(django_application)

from messaging.routing import application

