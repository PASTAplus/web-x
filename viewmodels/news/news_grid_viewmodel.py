#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: news_grid_viewmodel

:Synopsis:

:Author:
    servilla

:Created:
    4/6/2022
"""
from starlette.requests import Request

from services import news_service
from viewmodels.shared.viewmodel import ViewModelBase


class NewsGridViewModel(ViewModelBase):

    def __init__(self, request: Request, title: str = "Environmental Data Initiative"):
        super().__init__(request, title)
        self.grid_objects = news_service.get_grid_objects()
