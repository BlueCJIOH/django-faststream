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
subscribes to the `test-topic` Kafka topic. Incoming messages are logged to the
container output.

To publish a test message:

```bash
docker exec -it kafka kafka-console-producer.sh --bootstrap-server kafka:9092 --topic test-topic
>
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
