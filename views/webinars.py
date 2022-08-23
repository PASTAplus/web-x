#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: about

:Synopsis:

:Author:
    clarke

:Created:
    8/18/22
"""
import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.webinars.webinars_grid_viewmodel import WebinarsGridViewModel
from viewmodels.webinars.webinars_viewmodel import WebinarsViewModel

router = fastapi.APIRouter()


@router.get('/webinars/webinars-grid')
@template("webinars/webinars-grid.html")
def webinars_grid(request: Request):
    vm = WebinarsGridViewModel(request, "Webinars")
    return vm.to_dict()


@router.get('/webinars/{name}')
@template("webinars/webinars.html")
def webinars(request: Request, name: str):
    vm = WebinarsViewModel(request, f"Webinars - {name} ", name=name)
    return vm.to_dict()
