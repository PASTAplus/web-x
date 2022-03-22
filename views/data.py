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


@router.get('/data/discover')
@template("data/discover.html")
def discover(request: Request):
    vm = ViewModelBase(request, "Discover Data")
    return vm.to_dict()


@router.get('/data/publish-data')
@template("data/publish-data.html")
def publish(request: Request):
    vm = ViewModelBase(request, "Publish Data")
    return vm.to_dict()


@router.get('/data/featured')
@template("data/featured.html")
def featured(request: Request):
    vm = ViewModelBase(request, "Featured Data")
    return vm.to_dict()


@router.get('/data/example')
@template("data/example.html")
def example(request: Request):
    vm = ViewModelBase(request, "Example Data")
    return vm.to_dict()

@router.get('/data/featured_mar_2022')
@template("data/featured_mar_2022.html")
def featured_mar_2022(request: Request):
    vm = ViewModelBase(request, "Featured Data 3/2022")
    return vm.to_dict()
