#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: featured

:Synopsis:

:Author:
    servilla

:Created:
    4/5/22
"""
import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.featured.featured_grid_viewmodel import FeaturedGridViewModel
from viewmodels.featured.featured_viewmodel import FeaturedViewModel

router = fastapi.APIRouter()


@router.get('/featured/featured-grid')
@template("featured/featured-grid.html")
def featured_grid(request: Request):
    vm = FeaturedGridViewModel(request, "Featured Data")
    return vm.to_dict()


@router.get('/featured/{name}')
@template("featured/featured.html")
def featured(request: Request, name: str):
    vm = FeaturedViewModel(request, f"Featured Data - {name} ", name=name)
    return vm.to_dict()
