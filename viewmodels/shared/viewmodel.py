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

from services import cookie_auth


class ViewModelBase:

    def __init__(self, request: Request):
        self.request: Request = request
        self.error: Optional[str] = None
        self.user_id: Optional[str] = None

        self.is_logged_in, self.common_name = cookie_auth.get_user_via_auth_cookie(self.request)

    def to_dict(self) -> dict:
        return self.__dict__
