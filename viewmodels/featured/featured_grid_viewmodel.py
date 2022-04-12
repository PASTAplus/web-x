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
from starlette.requests import Request

from services.post_service import get_postcard_objects
from viewmodels.shared.viewmodel import ViewModelBase


class FeaturedGridViewModel(ViewModelBase):

    def __init__(self, request: Request, title: str = "Environmental Data Initiative"):
        super().__init__(request, title)
        self.grid_objects = get_postcard_objects(post_type="featured", clip_len=200, img_picker="pickme")
