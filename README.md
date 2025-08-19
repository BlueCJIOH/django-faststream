# Django FastStream Example

Minimal Django project configured to run FastStream with a Kafka broker.
The project structure follows the layout used in the
[education-backend](https://github.com/tough-dev-school/education-backend/)
repository: source code lives under `src/`, apps are kept inside `src/apps`,
and project configuration is stored in `src/core`.

The ASGI application is managed by
[`django-asgi-lifespan`](https://github.com/illagrenan/django-asgi-lifespan),
which exposes startup/shutdown events. A shared `httpx.AsyncClient` is
created at startup and injected into `request.state` so views can reuse it
without re-instantiating a client on each request.

## Requirements

- Docker
- Docker Compose
- Make

## Quick Start

Build and start the application with Kafka:

```bash
make up
```

The Django server will be available at <http://localhost:8000>.

## FastStream

The FastStream application is defined in `apps/faststream_app/stream.py` and
subscribes to the `test-topic` Kafka topic. Because Django's ASGI lifespan is
enabled, the FastStream process starts and stops with the Django server.
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
