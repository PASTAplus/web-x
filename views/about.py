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
def vision_mission(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()


@router.get('/about/team')
@template("about/team.html")
def team(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()


@router.get('/about/team/mark-servilla')
@template("about/team/mark-servilla.html")
def mark_servilla(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()
