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


@router.get('/support/help')
@template("support/support.html")
def support(request: Request):
    vm = ViewModelBase(request, "Support")
    return vm.to_dict()


@router.get('/support/faq')
@template("support/faq.html")
def faq(request: Request):
    vm = ViewModelBase(request, "Frequently Asked Questions")
    return vm.to_dict()

