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


@router.get('/resources/authors')
@template("resources/authors.html")
def authors(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()

@router.get('/resources/users')
@template("resources/users.html")
def users(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()

@router.get('/resources/data_managers')
@template("resources/data_managers.html")
def managers(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()
