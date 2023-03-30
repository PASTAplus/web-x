#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: tombstone_viewmodel

:Synopsis:

:Author:
    servilla

:Created:
    3/30/23
"""
from starlette.requests import Request

from viewmodels.shared.viewmodel import ViewModelBase


class TombstoneViewModel(ViewModelBase):
    def __init__(self, request: Request, title: str = "Environmental Data Initiative"):
        super().__init__(request, title)

        self.pid = None
        self.doi = None

    def load(self):
        if "pid" in self.request.query_params:
            self.pid = self.request.query_params["pid"].strip()
        if "doi" in self.request.query_params:
            self.doi = self.request.query_params["doi"].strip()
