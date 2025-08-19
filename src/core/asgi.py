import os
from contextlib import asynccontextmanager

from django_asgi_lifespan.asgi import get_asgi_application
from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

from apps.faststream_app.stream import broker


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")


django_asgi = get_asgi_application()


@asynccontextmanager
async def broker_lifespan(app):
    await broker.start()
    try:
        yield
    finally:
        await broker.close()


app = Starlette(
    routes=[
        Mount("/static", StaticFiles(directory="static"), name="static"),
        Mount("/", django_asgi),
    ],
    lifespan=broker_lifespan,
)

