# Nois-api

GraphQL API for the anonymous voice message board app Nois.


## Stack
- [Poetry](https://python-poetry.org/) for python packaging and dependency management
- [Starlette](https://www.starlette.io/) ASGI framework running on top of [Uvicorn](http://www.uvicorn.org/) ASGI server.
- [Graphene](https://graphene-python.org/) for GraphQL
- [Gino](https://python-gino.org/docs/en/1.0/index.html), a lightweight ORM for [Postgres](https://www.postgresql.org/) database.
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) for database migrations

## Installation, running, migrations
- Requirements: `python 3.8+` and `poetry`
- Run `poetry install` to install all dependencies and dev-dependencies
- Run `poetry run uvicorn poetry nois_api.main:app` to launch server. Add `--reload` flag for hot reloading.
- After changing Gino models, db migrations can be ran as follows:
  1. Generate revisions with `poetry run alembic revision --autogenerate -m 'Message describing the changes'`
  2. Check the generated revision files, fix things if not ok
  3. Run changes with `poetry run alembic upgrade head`
