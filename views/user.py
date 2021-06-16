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
from typing import Optional

import fastapi
from fastapi_chameleon import template
from starlette.requests import Request
import starlette.status as status

from services import cookie_auth, user_service
from viewmodels.user.login_viewmodel import LoginViewModel

router = fastapi.APIRouter()


@router.get('/user/login')
@template("user/login.html")
def login(request: Request, token: Optional[str] = None, cname: Optional[str] = None):
    vm = LoginViewModel(request)
    if token is None and cname is None:
        return vm.to_dict()
    elif token is None or cname is None:
        vm.error = "A failure occurred during privacy acceptance"
        return vm.to_dict()
    else:
        user = user_service.login_user_from_token(cname, token)
        if user is None:
            vm.error = "The account does not exist or the password is wrong"
            return vm.to_dict()
        resp = fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
        cookie_auth.set_auth(resp, user.user_id, user.common_name)
        return resp


@router.post('/user/login')
@template('user/login.html')
async def login(request: Request):

    vm = LoginViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    user, s = await user_service.login_user(vm.user_id, vm.password)
    if user is not None:
        resp = fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
        cookie_auth.set_auth(resp, user.user_id, user.common_name)
    elif s == status.HTTP_418_IM_A_TEAPOT:
        dn = f"uid={vm.user_id},o=EDI,dc=edirepository,dc=org"
        url = f"https://auth-d.edirepository.org/auth/accept?uid={dn}&target=web-x.edirepository.org/user/login"
        resp = fastapi.responses.RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
    else:
        vm.error = "The account does not exist or the password is wrong."
        return vm.to_dict()

    return resp


@router.get('/user/logout')
def logout():
    response = fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.logout(response)

    return response
