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


@router.get('/resources/edi-data-citations')
@template("resources/edi-data-citations.html")
def edi_data_citations(request: Request):
    vm = ViewModelBase(request, "EDI Data Citations")
    return vm.to_dict()


@router.get('/about/edi-public-calendar')
@template("about/edi-public-calendar.html")
def edi_public_calendar(request: Request):
    vm = ViewModelBase(request, "EDI Public Calendar")
    return vm.to_dict()


@router.get('/about/edi-affiliations')
@template("about/edi-affiliations.html")
def edi_affiliations(request: Request):
    vm = ViewModelBase(request, "About EDI Affiliations")
    return vm.to_dict()

@router.get('/about/data-sustainability')
@template("about/data-sustainability.html")
def data_sustainability(request: Request):
    vm = ViewModelBase(request, "Data Sustainability")
    return vm.to_dict()