.PHONY: build up down shell

build:
	docker compose build

up:
	docker compose up

down:
	docker compose down

shell:
	docker compose run --rm web bash
