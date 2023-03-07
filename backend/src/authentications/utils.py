from datetime import datetime, timedelta
from typing import Any

from jose import jwt

from . import constants


def create_token(subject: str | Any, secret: str, expires_delta: int) -> str:
    expires_delta = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, secret, constants.ALGORITHM)
    return encoded_jwt


def create_access_token(subject: str | Any, expires_delta: int = constants.ACCESS_TOKE_EXPIRE_MINUTES) -> str:
    encoded_jwt = create_token(subject=subject, expires_delta=expires_delta, secret=constants.JWT_SECRET_KEY)
    return encoded_jwt


def create_refresh_token(subject: str | Any, expires_delta: int = constants.REFRESH_TOKEN_EXPIRE_MINUTES) -> str:
    encoded_jwt = create_token(subject=subject, expires_delta=expires_delta, secret=constants.JWT_REFRESH_SECRET_KEY)
    return encoded_jwt


def is_refresh_token_valid(refresh_token: str) -> tuple[bool, str]:
    try:
        jwt_json = jwt.decode(token=refresh_token, key=constants.JWT_REFRESH_SECRET_KEY, algorithms=constants.ALGORITHM)
        return False, jwt_json["sub"]
    except jwt.ExpiredSignatureError:
        return True, ""
