from .app import app
from starlite import Starlite


def create_app() -> Starlite:
    return app
