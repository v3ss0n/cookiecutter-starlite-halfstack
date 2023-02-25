# Tutorial

## Step 1: Install Cookiecutter

Install cookiecutter:

``` bash
pip install cookiecutter
```

## Step 2: Generate Your Project

Now it's time to generate your starlite project.

Run the following command and feed with answers, If you don’t know what to enter, stick with the defaults:

```bash
cookiecutter https://github.com/waynerv/cookiecutter-pypackage.git
```

Finally, a new folder will be created under current folder, the name is the answer you
provided to `project_slug`.

## Step 3

Make sure docker is already up and usable.
Go into your project directory and :

- Rename `.env.example` to `.env`
- Start `docker compose up --build`
- visit `localhost:8000/schema/swagger`
