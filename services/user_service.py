#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: user_service

:Synopsis:

:Author:
    servilla

:Created:
    6/9/21
"""
from typing import Optional

from data.user import User


def login_user(user_id: str, password: str) -> Optional[User]:
    # TODO: Perform login via auth.edirepository.org

    common_name: str = "Mark Servilla"
    user_id: str = "mark.servilla@gmail.com"
    password: str = "BlahBlah"

    return User(common_name, user_id, password)
