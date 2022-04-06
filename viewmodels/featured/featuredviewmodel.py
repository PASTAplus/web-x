#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: viewmodel

:Synopsis:

:Author:
    servilla

:Created:
    5/25/21
"""
from typing import Optional

from starlette.requests import Request

from services import featured_data_service
from viewmodels.shared.viewmodel import ViewModelBase


class FeaturedViewModel(ViewModelBase):

    def __init__(self, request: Request, title: str = "Environmental Data Initiative", name=None):
        super().__init__(request, title)
        self.main = featured_data_service.get_html(name)
        pass

    def to_dict(self) -> dict:
        return self.__dict__
