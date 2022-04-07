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

from viewmodels.news.news_grid_viewmodel import NewsGridViewModel
from viewmodels.news.news_viewmodel import NewsViewModel

router = fastapi.APIRouter()


@router.get('/news/news-grid')
@template("news/news-grid.html")
def news_grid(request: Request):
    vm = NewsGridViewModel(request, "News")
    return vm.to_dict()


@router.get('/news/{name}')
@template("news/news.html")
def news(request: Request, name: str):
    vm = NewsViewModel(request, f"News - {name} ", name=name)
    return vm.to_dict()