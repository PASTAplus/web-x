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


@router.get('/about/vision-mission')
@template("about/vision-mission.html")
def about(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()


@router.get('/about/team')
@template("about/team.html")
def about(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()

@router.get('/about/team/mark')
@template("about/team/mark.html")
def about(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()
