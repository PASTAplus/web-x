#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: user

:Synopsis:

:Author:
    servilla

:Created:
    6/9/21
"""


class User:

    def __init__(self, user_id, common_name, auth_token):
        self.user_id: str = user_id
        self.common_name: str = common_name
        self.auth_token: str = auth_token
