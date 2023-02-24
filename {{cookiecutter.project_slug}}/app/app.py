from starlite import Starlite, get

from starlite_saqlalchemy import ConfigureApp
from app.controllers import authors

app = Starlite(route_handlers=[authors.create_router()], on_app_init=[ConfigureApp()])
