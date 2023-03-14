# Simplified starter with Cookiecutter For Starlite + SAQ + Sqlalchemy + Docker

This is starter with cookiecutter for Starlite.
It is much simpler version of <https://github.com/starlite-api/starlite-pg-redis-docker> 
Built on top of peter's <https://github.com/topsport-com-au/starlite-saqlalchemy>

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```
pip install -U cookiecutter
```

Generate a Python package project:

```
cookiecutter https://github.com/v3ss0n/cookiecutter-starlite-halfstack

```

Then follow **[Tutorial](docs/tutorial.md)** to finish other configurations.

## Features
- Easy to use ORM provided by starlite-saqlalchemy
- Alembic support For data Migrations
- Background Processing using SAQ
- Moked Mail Sending and Reciving with MailHog
- Fully running inside Docker Containers vid docker-compose



# Credits

[starlite-pg-redis-docker](https://github.com/starlite-api/starlite-pg-redis-docker)

[starlite-saqlalchemy](https://github.com/topsport-com-au/starlite-saqlalchemy)


Cookiecutter template is forked from [zillionare/python-project-wizard](https://github.com/zillionare/python-project-wizard), 
which originally forked from [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
