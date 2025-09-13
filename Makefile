.PHONY: run test fmt lint migrate

run:
	uvicorn gdhub.main:app --reload --app-dir src

test:
	PYTHONPATH=src pytest

fmt:
	black src tests

lint:
	ruff check src tests

migrate:
	alembic upgrade head
