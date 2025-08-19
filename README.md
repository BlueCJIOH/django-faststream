# Django FastStream Example

Minimal Django project configured to run FastStream with a Kafka broker.
The project structure follows the layout used in the
[education-backend](https://github.com/tough-dev-school/education-backend/)
repository: source code lives under `src/`, apps are kept inside `src/apps`,
and project configuration is stored in `src/core`.

Django is served through a tiny `Starlette` wrapper that also exposes a
lifespan context. The `lifespan` is used to start and stop the Kafka
`FastStream` broker alongside Django and to provide access to state objects
registered via [`django-asgi-lifespan`](https://github.com/illagrenan/django-asgi-lifespan).
Static assets are collected into `src/static/` and served by Starlette's
efficient static files handler.

## Requirements

- Docker
- Docker Compose
- Make

## Quick Start

Build and start the application with Kafka:

```bash
make up
```

The command runs `collectstatic` and starts Uvicorn. The Django server will be
available at <http://localhost:8000>.

## FastStream

The FastStream broker is defined in `apps/faststream_app/stream.py` and
subscribes to the `test-topic` Kafka topic. It is started and stopped in the
Starlette lifespan so it shares the lifecycle of the Django server.
Incoming messages are logged to the container output.

Use the Django REST Framework endpoint to publish a test message:

```bash
curl -X POST http://localhost:8000/publish/ -H "Content-Type: application/json" \
  -d '{"message": "hello"}'
```

## Development

Useful make targets:

- `make build` – build the Docker images
- `make up` – start Django and Kafka
- `make down` – stop services
- `make shell` – open a shell inside the Django container

## Project layout

```
├── Dockerfile
├── Makefile
├── docker-compose.yml
├── pyproject.toml
└── src
    ├── apps
    │   ├── faststream_app
    │   │   └── stream.py
    │   └── sample
    │       ├── apps.py
    │       ├── context.py
    │       ├── urls.py
    │       └── views.py
    ├── core
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py
```

## Testing

Run Django system checks:

```bash
uv run python manage.py check
```
