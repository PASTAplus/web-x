#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: featuredgridviewmodel

:Synopsis:

:Author:
    servilla

:Created:
    4/6/2022
"""
from typing import Optional

from starlette.requests import Request

from services import featured_service
from viewmodels.shared.viewmodel import ViewModelBase


class FeaturedGridViewModel(ViewModelBase):

    def __init__(self, request: Request, title: str = "Environmental Data Initiative"):
        super().__init__(request, title)
        self.grid_objects = featured_service.get_grid_objects()
