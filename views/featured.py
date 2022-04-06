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

from pathlib import Path

import fastapi
import fastapi_chameleon
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.featured.featuredviewmodel import FeaturedViewModel

router = fastapi.APIRouter()


@router.get('/featured/{name}')
@template("featured/featured.html")
def featured(request: Request, name: str):
    vm = FeaturedViewModel(request, f"Featured Data - {name} ", name=name)
    return vm.to_dict()

