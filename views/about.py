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


@router.get('/about/about-edi')
@template("about/about-edi.html")
def edi(request: Request):
    vm = ViewModelBase(request, "About EDI")
    return vm.to_dict()


@router.get('/about/edi-policy')
@template("about/edi-policy.html")
def policies(request: Request):
    vm = ViewModelBase(request, "About Policies")
    return vm.to_dict()


@router.get('/about/partners-and-affiliations')
@template("about/partners-and-affiliations.html")
def partners(request: Request):
    vm = ViewModelBase(request, "About Partners and Affiliations")
    return vm.to_dict()

@router.get('/about/edi-products')
@template("about/edi-products.html")
def partners(request: Request):
    vm = ViewModelBase(request, "EDI Products")
    return vm.to_dict()
