from aiohttp import web
from server.routes import setup_routes

import pathlib
import aiohttp_jinja2
import jinja2
BASE_DIR = pathlib.Path(__file__).parent


app = web.Application()
setup_routes(app)
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader(str(BASE_DIR /'templates')))
web.run_app(app)
