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
import fastapi
from fastapi_chameleon import template
from starlette.requests import Request
import starlette.status as status

from services import cookie_auth, user_service
from viewmodels.user.login_viewmodel import LoginViewModel

router = fastapi.APIRouter()


@router.get('/user/login')
@template("user/login.html")
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.post('/user/login')
@template('user/login.html')
async def login(request: Request):

    vm = LoginViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    user = user_service.login_user(vm.user_id, vm.password)
    if not user:
        vm.error = "The account does not exist or the password is wrong."
        return vm.to_dict()

    resp = fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(resp, user.user_id, user.common_name)

    return resp


@router.get('/user/logout')
def logout():
    response = fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.logout(response)

    return response
