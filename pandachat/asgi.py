import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pandachat.settings")

import django
django.setup()

from django.core.management import call_command
import room.routing


from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                room.routing.websocket_urlpatterns
            )
        ),
    ),
})
