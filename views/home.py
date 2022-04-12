#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: about

:Synopsis:

:Author:
    servilla

:Created:
    5/25/21
"""
import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.index_viewmodel import IndexViewModel

router = fastapi.APIRouter()


@router.get('/')
@template("index.html")
def index(request: Request):
    vm = IndexViewModel(request, "Environmental Data Initiative")
    return vm.to_dict()
