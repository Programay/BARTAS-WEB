from datetime import UTC, datetime, timedelta

from jose import ExpiredSignatureError, jwt

from backend.src.authentications import constants
from backend.src.users.schemas import SubjectSchema


def create_token(subject: SubjectSchema, secret: str, expires_delta: int) -> str:
    payload = {"exp": datetime.now(UTC) + timedelta(minutes=expires_delta)}
    payload.update(subject)
    encoded_jwt: str = jwt.encode(
        claims=payload, key=secret, algorithm=constants.ALGORITHM
    )
    return encoded_jwt


def create_access_token(
    subject: SubjectSchema, expires_delta: int = constants.ACCESS_TOKE_EXPIRE_MINUTES
) -> str:
    encoded_jwt = create_token(
        subject=subject, expires_delta=expires_delta, secret=constants.JWT_SECRET_KEY
    )
    return encoded_jwt


def create_refresh_token(
    subject: SubjectSchema, expires_delta: int = constants.REFRESH_TOKEN_EXPIRE_MINUTES
) -> str:
    encoded_jwt = create_token(
        subject=subject,
        expires_delta=expires_delta,
        secret=constants.JWT_REFRESH_SECRET_KEY,
    )
    return encoded_jwt


def is_refresh_token_valid(refresh_token: str) -> tuple[bool, SubjectSchema | None]:
    try:
        jwt_json = jwt.decode(
            token=refresh_token,
            key=constants.JWT_REFRESH_SECRET_KEY,
            algorithms=constants.ALGORITHM,
        )
        return False, SubjectSchema(**jwt_json)
    except ExpiredSignatureError:
        return True, None
