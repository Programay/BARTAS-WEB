from jose import jwt
from jose.exceptions import JOSEError
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from .authentications.constants import JWT_SECRET_KEY

security = HTTPBearer()


async def has_access(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        jwt.decode(token, key=JWT_SECRET_KEY, options={"verify_signature": False,
                                                                 "verify_aud": False,
                                                                 "verify_iss": False})
    except JOSEError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))

