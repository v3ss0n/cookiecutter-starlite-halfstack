# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}
## Features

This is starter  for [Starlite](https://github.com/starlite-api/starlite)  and much simpler version of <https://github.com/starlite-api/starlite-pg-redis-docker> , using peter's <https://github.com/topsport-com-au/starlite-saqlalchemy>

Starlite:

[Starlite documentation 📚](https://starlite-api.github.io/starlite/)

starlite-saqslalchmey:
<https://github.com/topsport-com-au/starlite-saqlalchemy>

## Run the application

### Setup

* `$ cp .env.example .env`
* `$ docker-compose build`
* `$ docker-compose run --rm app alembic upgrade head`

### Run

`$ docker-compose up --build`

### Async Worker Emails

To demonstrate usage of the asynchronous `SAQ` workers, when an `Author` is created we trigger a
worker function that sends an email.

`mailhog` is included in `docker-compose.yaml`, and includes a GUI that can be accessed at
`http://localhost:8025`.

Create an `Author`:

```bash
$ curl -w "\n" -X POST -H "Content-Type: application/json" -d '{"name": "James Patterson", "dob": "1974-3-22"}' http://localhost:8000/v1/authors
{"id":"6f395bdf-3e77-481d-98b2-3471c2342654","created":"2022-10-09T23:18:10","updated":"2022-10-09T23:18:10","name":"James Patterson","dob":"1974-03-22"}
```

Then check the `mailhog` GUI to see the email that has been sent by the worker.

### Migrations

#### Revision

`$ docker-compose run --rm app alembic revision --autogenerate -m "revision description"`

#### Migration

`$ docker-compose run --rm app alembic upgrade head`
