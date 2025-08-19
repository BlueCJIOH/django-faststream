import os
from django_asgi_lifespan.asgi import get_asgi_application
from apps.faststream_app.stream import faststream_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application(lifespan=faststream_app.lifespan)
