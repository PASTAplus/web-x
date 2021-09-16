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


@router.get('/about/edi')
@template("about/edi.html")
def edi(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()

@router.get('/about/policies')
@template("about/policies.html")
def policies(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()

@router.get('/about/edi/team')
@template("about/edi/team.html")
def mark_servilla(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()
