#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: home

:Synopsis:

:Author:
    servilla

:Created:
    5/25/21
"""
import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.home.indexviewmodel import IndexViewModel
from viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


@router.get('/')
@template("home/index.html")
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()


@router.get('/about')
@template("templates/home/about.html")
def about(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()
