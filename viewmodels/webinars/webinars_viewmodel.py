#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: webinars_viewmodel

:Synopsis:

:Author:
    clarke

:Created:
    8/18/2022
"""
from typing import Optional

from starlette.requests import Request

from services.post_service import get_post_html
from viewmodels.shared.viewmodel import ViewModelBase


class WebinarsViewModel(ViewModelBase):

    def __init__(self, request: Request, title: str = "Environmental Data Initiative", name=None):
        super().__init__(request, title)
        self.main = get_post_html("webinars", name)
