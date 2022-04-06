#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: main.py

:Synopsis:

:Author:
    servilla

:Created:
    5/14/21
"""
import logging
import os

import daiquiri
import fastapi
import fastapi_chameleon
import uvicorn
from starlette.staticfiles import StaticFiles

from views import about
from views import resources
from views import support
from views import data
from views import home
from views import user
from views import search
from views import featured

cwd = os.path.dirname(os.path.realpath(__file__))
logfile = cwd + "/web-x.log"
daiquiri.setup(level=logging.INFO,
               outputs=(daiquiri.output.File(logfile), "stdout",))
logger = daiquiri.getLogger(__name__)


app = fastapi.FastAPI()


def configure(dev_mode: bool):
    configure_templates(dev_mode)
    configure_routes()


def configure_templates(dev_mode: bool):
    fastapi_chameleon.global_init('templates', auto_reload=dev_mode)


def configure_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(about.router)
    app.include_router(resources.router)
    app.include_router(data.router)
    app.include_router(support.router)
    app.include_router(home.router)
    app.include_router(user.router)
    app.include_router(search.router)
    app.include_router(featured.router)


if __name__ == "__main__":
    configure(dev_mode=True)
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)
else:
    configure(dev_mode=False)
