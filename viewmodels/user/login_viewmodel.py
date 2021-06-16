#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: login_viewmodel

:Synopsis:

:Author:
    servilla

:Created:
    6/9/21
"""
from starlette.requests import Request

from viewmodels.shared.viewmodel import ViewModelBase


class LoginViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.user_id = ''
        self.password = ''

    async def load(self):
        form = await self.request.form()
        self.user_id = form.get('user_id', '').lower().strip()
        self.password = form.get('password', '').strip()

        if not self.user_id or not self.user_id.strip():
            self.error = 'You must specify a user id.'
        elif not self.password:
            self.error = 'You must specify a password.'
