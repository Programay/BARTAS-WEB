from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..users import schemas, services
from ..users.utils import verify_password
from .exceptions import InvalidCredentialException, InvalidTokenException
from .utils import create_access_token, create_refresh_token, is_refresh_token_valid

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/tokens")
async def tokens(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = services.get_user_by_username(db, username=user.username)
    if db_user is None:
        raise InvalidCredentialException()

    if not verify_password(hashed_password=db_user.password, password=user.password):
        raise InvalidCredentialException()

    return {
        "access_token": create_access_token(
            subject={"username": db_user.username, "is_staff": db_user.is_staff}
        ),
        "refresh_token": create_refresh_token(
            subject={"username": db_user.username, "is_staff": db_user.is_staff}
        ),
    }


@router.post("/tokens/refresh")
async def tokens_refresh(token: str):
    is_expired, subject = is_refresh_token_valid(token)
    if is_expired:
        raise InvalidTokenException()
    else:
        return {"access_token": create_access_token(subject)}
