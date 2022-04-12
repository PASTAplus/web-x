#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: index_viewmodel

:Synopsis:

:Author:
    servilla

:Created:
    5/25/21
"""
from typing import List

from starlette.requests import Request

from services import post_service
from viewmodels.shared.viewmodel import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request, title: str = "Environmental Data Initiative"):
        super().__init__(request, title)

        self.featured = post_service.get_postcard_objects(post_type="featured", clip_len=200, img_picker="pickme")
        self.news = post_service.get_postcard_objects(post_type="news", clip_len=200, img_picker="pickme")
