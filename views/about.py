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
    vm = ViewModelBase(request, "About EDI")
    return vm.to_dict()


@router.get('/about/policies')
@template("about/policies.html")
def policies(request: Request):
    vm = ViewModelBase(request, "About Policies")
    return vm.to_dict()


@router.get('/about/partners')
@template("about/partners.html")
def partners(request: Request):
    vm = ViewModelBase(request, "About Partners")
    return vm.to_dict()


@router.get('/about/services')
@template("about/services.html")
def services(request: Request):
    vm = ViewModelBase(request, "About Services")
    return vm.to_dict()
