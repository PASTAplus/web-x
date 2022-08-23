#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: webinars_grid_viewmodel

:Synopsis:

:Author:
    clarke

:Created:
    8/18/2022
"""
from starlette.requests import Request

from services.post_service import get_postcard_objects
from viewmodels.shared.viewmodel import ViewModelBase


class WebinarsGridViewModel(ViewModelBase):

    def __init__(self, request: Request, title: str = "Environmental Data Initiative"):
        super().__init__(request, title)
        self.grid_objects = get_postcard_objects(post_type="webinars", clip_len=None, img_picker="pickme")
