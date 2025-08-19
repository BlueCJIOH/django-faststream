import os
from contextlib import asynccontextmanager
import asyncio

from django_asgi_lifespan.asgi import get_asgi_application
from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

from apps.faststream_app.stream import broker


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")


django_asgi = get_asgi_application()


@asynccontextmanager
async def broker_lifespan(app):
    last_error: Exception | None = None
    for attempt in range(20):
        try:
            await broker.start()
            last_error = None
            break
        except Exception as exc:  # aiokafka raises various connection errors
            last_error = exc
            await asyncio.sleep(3)
    if last_error is not None:
        raise last_error
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

