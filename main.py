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

from config import Config
from views import about
from views import resources
from views import support
from views import data
from views import index
from views import user
from views import search
from views import featured
from views import news
from views import webinars


daiquiri.setup(level=logging.INFO,
               outputs=(daiquiri.output.File(Config.LOGFILE), "stdout",))
logger = daiquiri.getLogger(__name__)


app = fastapi.FastAPI(docs_url=None, redoc_url=None)


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
    app.include_router(index.router)
    app.include_router(user.router)
    app.include_router(search.router)
    app.include_router(featured.router)
    app.include_router(news.router)
    app.include_router(webinars.router)


if __name__ == "__main__":
    configure(dev_mode=True)
    uvicorn.run(app, host='127.0.0.1', port=8000)
else:
    configure(dev_mode=False)
