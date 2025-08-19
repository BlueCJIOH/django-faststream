import os
from django_asgi_lifespan.asgi import get_asgi_application
from apps.faststream_app.stream import faststream_app

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

django_application = get_asgi_application(lifespan=faststream_app.lifespan)


async def application(scope, receive, send):
    if scope["type"] in {"http", "lifespan"}:
        await django_application(scope, receive, send)
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")
