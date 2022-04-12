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

from services.post_service import get_post_html
from viewmodels.shared.viewmodel import ViewModelBase


class NewsViewModel(ViewModelBase):

    def __init__(self, request: Request, title: str = "Environmental Data Initiative", name=None):
        super().__init__(request, title)
        self.main = get_post_html("news", name)
