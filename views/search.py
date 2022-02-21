#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: search.html

:Synopsis:

:Author:
    servilla

:Created:
    2/13/22
"""
from typing import Optional

import fastapi
from fastapi_chameleon import template
from starlette.requests import Request
import starlette.status as status

from viewmodels.search.search_viewmodel import SearchViewModel
from viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


@router.post('/search')
@template('search/search.html')
async def search(request: Request):

    vm = SearchViewModel(request, "Website Search")
    await vm.load()

    if vm.error:
        return fastapi.responses.RedirectResponse(url=vm.referer, status_code=status.HTTP_302_FOUND)

    return vm.to_dict()
