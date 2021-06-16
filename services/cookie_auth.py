import hashlib
from typing import Optional

from fastapi import Request
from fastapi import Response


auth_cookie_name = 'edi_account'


def set_auth(response: Response, user_id: str, common_name: str):
    hash_val = __hash_text(user_id + common_name)
    val = f"{user_id}:{common_name}:{hash_val}"
    response.set_cookie(auth_cookie_name, val, secure=False, httponly=True, samesite='Lax')


def __hash_text(text: str) -> str:
    text = 'salty__' + text + '__text'
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_user_via_auth_cookie(request: Request) -> Optional[tuple]:
    if auth_cookie_name not in request.cookies:
        return None, None

    val = request.cookies[auth_cookie_name]
    parts = val.split(':')
    if len(parts) != 3:
        return None, None

    user_id = parts[0]
    common_name = parts[1]
    hash_val = parts[2]
    hash_val_check = __hash_text(user_id + common_name)
    if hash_val != hash_val_check:
        print("Warning: Hash mismatch, invalid cookie value")
        return None, None

    return user_id, common_name


def logout(response: Response):
    response.delete_cookie(auth_cookie_name)
