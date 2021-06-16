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
import base64
from typing import Optional

import aiohttp
import daiquiri
import starlette.status as status

from data.user import User


logger = daiquiri.getLogger(__name__)


async def login_user(user_id: str, password: str) -> (Optional[User], int):

    url = "https://auth-d.edirepository.org/auth/login/pasta"
    dn = f"uid={user_id},o=EDI,dc=edirepository,dc=org"
    authorization = (base64.b64encode(f"{dn}:{password}".encode("utf-8"))).decode("utf-8")
    headers = {"authorization": "Basic " + authorization}

    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as resp:
            s = resp.status

    if s == status.HTTP_200_OK:
        cookies = resp.cookies
        auth_token = cookies["auth-token"]
        common_name = user_id
        return User(user_id, common_name, auth_token), s
    elif s == status.HTTP_400_BAD_REQUEST:
        msg = "Basic Authorization header not sent in request"
        logger.error(msg)
        return None, s
    elif s == status.HTTP_401_UNAUTHORIZED:
        return None, s
    elif s == status.HTTP_418_IM_A_TEAPOT:
        return None, s
    else:
        msg = "Unrecognized error occurred - response status code: {s}"
        logger.error(msg)
        return None, s


def login_user_from_token(common_name: str, auth_token: str) -> Optional[User]:
    return User(user_id=common_name, common_name=common_name, auth_token=auth_token)
