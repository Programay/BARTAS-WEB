from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt
from jose.exceptions import JOSEError

from .authentications.constants import JWT_SECRET_KEY

security = HTTPBearer()


async def has_access(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        jwt.decode(
            token,
            key=JWT_SECRET_KEY,
            options={
                "verify_signature": False,
                "verify_aud": False,
                "verify_iss": False,
            },
        )
    except JOSEError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))


async def has_staff_access(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials

    try:
        jwt_json = jwt.decode(
            token,
            key=JWT_SECRET_KEY,
            options={
                "verify_signature": False,
                "verify_aud": False,
                "verify_iss": False,
            },
        )
        is_user_staff = jwt_json["is_staff"]
        if not is_user_staff:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Permission Denied"
            )

    except JOSEError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
