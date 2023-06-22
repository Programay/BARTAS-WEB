from datetime import datetime, timedelta

from jose import jwt

from . import constants


def create_token(subject: dict, secret: str, expires_delta: int) -> str:
    expires_delta = datetime.utcnow() + timedelta(minutes=expires_delta)
    payload = {"exp": expires_delta}
    payload.update(subject)
    encoded_jwt = jwt.encode(claims=payload, key=secret, algorithm=constants.ALGORITHM)
    return encoded_jwt


def create_access_token(subject: dict, expires_delta: int = constants.ACCESS_TOKE_EXPIRE_MINUTES) -> str:
    encoded_jwt = create_token(subject=subject, expires_delta=expires_delta, secret=constants.JWT_SECRET_KEY)
    return encoded_jwt


def create_refresh_token(subject: dict, expires_delta: int = constants.REFRESH_TOKEN_EXPIRE_MINUTES) -> str:
    encoded_jwt = create_token(subject=subject, expires_delta=expires_delta, secret=constants.JWT_REFRESH_SECRET_KEY)
    return encoded_jwt


def is_refresh_token_valid(refresh_token: str) -> tuple[bool, dict]:
    try:
        jwt_json = jwt.decode(token=refresh_token, key=constants.JWT_REFRESH_SECRET_KEY, algorithms=constants.ALGORITHM)
        return False, jwt_json
    except jwt.ExpiredSignatureError:
        return True, {}
