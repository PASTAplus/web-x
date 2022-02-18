#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: search_viewmodel

:Synopsis:

:Author:
    servilla

:Created:
    2/13/22
"""
from starlette.requests import Request

import services.search_service as search_service
from viewmodels.shared.viewmodel import ViewModelBase


class SearchViewModel(ViewModelBase):
    def __init__(self, request: Request, title: str = "Environmental Data Initiative"):
        super().__init__(request, title)

        self.pages = None
        self.referer = None
        self.terms = ''

    async def load(self):
        form = await self.request.form()
        self.terms = form.get('terms', '').strip()
        headers = self.request.headers
        self.referer = headers["referer"]

        if not self.terms or not self.terms.strip():
            self.error = True
        else:
            self.pages = search_service.search_on_terms(self.terms)
