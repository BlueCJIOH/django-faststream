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
