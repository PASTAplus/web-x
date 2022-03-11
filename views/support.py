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


@router.get('/support/contact-us')
@template("support/contact-us.html")
def support(request: Request):
    vm = ViewModelBase(request, "Contact Us")
    return vm.to_dict()


@router.get('/support/frequently-asked-questions')
@template("support/frequently-asked-questions.html")
def faq(request: Request):
    vm = ViewModelBase(request, "Frequently Asked Questions")
    return vm.to_dict()

