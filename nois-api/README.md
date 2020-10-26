# Nois-api

GraphQL API for the anonymous voice message board app Nois.


## Stack
- [Poetry](https://python-poetry.org/) for python packaging and dependency management
- [Starlette](https://www.starlette.io/) ASGI framework running on top of [Uvicorn](http://www.uvicorn.org/) ASGI server.
- [Ariadne](https://ariadnegraphql.org) GraphQL server
- [Edgedb](https://www.edgedb.com/) Database

## Installation, running, migrations
- Requirements: `python 3.8+` and `poetry`
- Run `poetry install` to install all dependencies
- Run `poetry run uvicorn nois_api.main:app` to launch server. Add `--reload` flag for hot reloading.

## Tests

- Code errors can be checked with `poetry run flake8 .`
- Code style errors can be checked with `poetry run black --check .`


TODO:
- graphql initializing
