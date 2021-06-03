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
import fastapi
import fastapi_chameleon
import uvicorn
from starlette.staticfiles import StaticFiles

from views import home

app = fastapi.FastAPI()


def configure(dev_mode: bool):
    configure_templates(dev_mode)
    configure_routes()


def configure_templates(dev_mode: bool):
    fastapi_chameleon.global_init('templates', auto_reload=dev_mode)


def configure_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)


if __name__ == "__main__":
    configure(dev_mode=True)
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)
else:
    configure(dev_mode=False)