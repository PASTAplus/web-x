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


@router.get('/support/dm-fellowships')
@template("support/dm-fellowships.html")
def fellowships(request: Request):
    vm = ViewModelBase(request, "EDI Data Management Fellowship Program")
    return vm.to_dict()


@router.get('/support/faq-fellowships')
@template("support/faq-fellowships.html")
def fellowships(request: Request):
    vm = ViewModelBase(request, "Fellowship Program - Frequently Asked Questions")
    return vm.to_dict()


@router.get('/support/fellowship-2018')
@template("support/fellowship-2018.html")
def fellowships(request: Request):
    vm = ViewModelBase(request, "2018 Fellowship Program")
    return vm.to_dict()


@router.get('/support/fellowship-2019')
@template("support/fellowship-2019.html")
def fellowships(request: Request):
    vm = ViewModelBase(request, "2019 Fellowship Program")
    return vm.to_dict()


@router.get('/support/fellowship-2020')
@template("support/fellowship-2020.html")
def fellowships(request: Request):
    vm = ViewModelBase(request, "2020 Fellowship Program")
    return vm.to_dict()


@router.get('/support/fellowship-2021')
@template("support/fellowship-2021.html")
def fellowships(request: Request):
    vm = ViewModelBase(request, "2021 Fellowship Program")
    return vm.to_dict()

@router.get('/support/fellowship-2022')
@template("support/fellowship-2022.html")
def fellowships(request: Request):
    vm = ViewModelBase(request, "2022 Fellowship Program")
    return vm.to_dict()

@router.get('/support/frequently-asked-questions')
@template("support/frequently-asked-questions.html")
def faq(request: Request):
    vm = ViewModelBase(request, "Frequently Asked Questions")
    return vm.to_dict()
