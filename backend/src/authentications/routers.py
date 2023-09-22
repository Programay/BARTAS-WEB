from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..users import schemas as user_schemas
from ..users import services
from ..users.utils import verify_password
from . import schemas
from .exceptions import InvalidCredentialException, InvalidTokenException
from .utils import create_access_token, create_refresh_token, is_refresh_token_valid

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def tokens(
    user: user_schemas.UserLogin, db: Session = Depends(get_db)
) -> schemas.LoginResponse:
    db_user = services.get_user_by_username(db, username=user.username)
    if db_user is None:
        raise InvalidCredentialException()

    if not verify_password(hashed_password=db_user.password, password=user.password):
        raise InvalidCredentialException()

    access_token = create_access_token(
        subject={"username": db_user.username, "is_staff": db_user.is_staff}
    )
    refresh_token = create_refresh_token(
        subject={"username": db_user.username, "is_staff": db_user.is_staff}
    )

    return schemas.LoginResponse(access_token=access_token, refresh_token=refresh_token)


@router.post("/login/refresh")
async def tokens_refresh(token: str) -> schemas.RefreshLoginResponse:
    is_expired, subject = is_refresh_token_valid(token)
    if is_expired:
        raise InvalidTokenException()
    else:
        access_token = create_access_token(subject)
        return schemas.RefreshLoginResponse(access_token=access_token)
