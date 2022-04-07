#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: indexviewmodel

:Synopsis:

:Author:
    servilla

:Created:
    5/25/21
"""
from typing import List

from starlette.requests import Request

from services import package_service
from viewmodels.shared.viewmodel import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.package_count: int = package_service.package_count()
        self.packages: List = package_service.latest_packages(limit=5)
