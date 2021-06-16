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

    def __init__(self, common_name, user_id, password):
        self.user_id: str = user_id
        self.common_name: str = common_name
        self.password: str = password
