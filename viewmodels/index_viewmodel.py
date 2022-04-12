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

from viewmodels.shared.viewmodel import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

