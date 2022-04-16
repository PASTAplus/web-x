#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: about

:Synopsis:

:Author:
    servilla

:Created:
    6/3/21
"""
import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


@router.get('/data/publish-data')
@template("data/publish-data.html")
def publish(request: Request):
    vm = ViewModelBase(request, "Publish Data")
    return vm.to_dict()


@router.get('/data/find-data')
@template("data/find-data.html")
def find(request: Request):
    vm = ViewModelBase(request, "Find Data")
    return vm.to_dict()
