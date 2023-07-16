from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from .consumers import ChatConsumer


websocket_urlpatterns = [
  path('chat/', ChatConsumer.as_asgi(), name='chat'),
]

application = ProtocolTypeRouter(
  {
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
  }
)