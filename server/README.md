# Server

This folder contains source for Nois server. Following technologies are used:
- [Python](https://www.python.org/), main language
- [Poetry](https://python-poetry.org/), dependency management
- [Starlette](https://www.starlette.io/), ASGI framework for building the server app itself
- [Uvicorn](http://www.uvicorn.org/), ASGI server running the app built with Starlette
- [Ariadne](https://ariadnegraphql.org), GraphQL app plugged to Starlette
- [Edgedb](https://www.edgedb.com/), object-relational database

## Installation

Prerequisites:
- Python, 3.8+
- Poetry, 1.0.10+
- Docker and docker-compose, at least docker-compose version 3 supported

Install project by running `poetry install`.

## Usage

- Run `docker-compose up` to start edgedb. Add `-d` flag to run it in background.
- Run `poetry run uvicorn server:app` to launch the server. Add `--reload` flag for hot reloading.
- Server is now running in [localhost port 8000](http://localhost:8000)
  - GraphQL playground can be found from [/graphql](http://localhost:8000/graphql) address.
    - Unfortunately playground provided by Ariadne doesn't support GraphQL file uploads, but you can use [altair](https://altair.sirmuel.design/) instead

## App structure

- Coming later

## Tests and checks

- Code errors can be checked with `poetry run flake8 .`
- Code style errors can be checked with `poetry run black --check .`
- Settings for flake8 and black can be found from `setup.cfg`
