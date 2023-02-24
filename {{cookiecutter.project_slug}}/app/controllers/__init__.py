from starlite import Router

from . import authors

__all__ = ["router"]

router = Router(path="/v1", route_handlers=[authors.create_router()])
