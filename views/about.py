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
def about_edi(request: Request):
    vm = ViewModelBase(request, "About EDI")
    return vm.to_dict()


@router.get('/about/edi-advisory-board')
@template("about/edi-advisory-board.html")
def edi_advisory_board(request: Request):
    vm = ViewModelBase(request, "EDI Advisory Board")
    return vm.to_dict()


@router.get('/about/edi-policy')
@template("about/edi-policy.html")
def edi_policy(request: Request):
    vm = ViewModelBase(request, "About Policies")
    return vm.to_dict()


@router.get('/about/edi-products')
@template("about/edi-products.html")
def edi_products(request: Request):
    vm = ViewModelBase(request, "EDI Products")
    return vm.to_dict()


@router.get('/about/edi-public-calendar')
@template("about/edi-public-calendar.html")
def edi_public_calendar(request: Request):
    vm = ViewModelBase(request, "EDI Public Calendar")
    return vm.to_dict()


@router.get('/about/partners-and-affiliations')
@template("about/partners-and-affiliations.html")
def partners_and_affiliations(request: Request):
    vm = ViewModelBase(request, "About Partners and Affiliations")
    return vm.to_dict()