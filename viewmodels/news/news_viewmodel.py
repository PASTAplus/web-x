#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: news_viewmodel

:Synopsis:

:Author:
    servilla

:Created:
    4/5/2022
"""
from typing import Optional

from starlette.requests import Request

from services import news_service
from viewmodels.shared.viewmodel import ViewModelBase


class NewsViewModel(ViewModelBase):

    def __init__(self, request: Request, title: str = "Environmental Data Initiative", name=None):
        super().__init__(request, title)
        self.main = news_service.get_html(name)

    def to_dict(self) -> dict:
        return self.__dict__
