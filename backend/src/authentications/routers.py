from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .utils import create_access_token, create_refresh_token, is_refresh_token_valid
from ..database import get_db
from ..users import schemas
from ..users import services
from ..users.utils import verify_password

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post('/tokens')
async def tokens(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = services.get_user_by_username(db, username=user.username)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")

    if not verify_password(hashed_password=db_user.password, password=user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")

    return {
        "access_token": create_access_token(subject={"username": db_user.username, "is_staff": db_user.is_staff}),
        "refresh_token": create_refresh_token(subject={"username": db_user.username, "is_staff": db_user.is_staff}),
    }


@router.post('/tokens/refresh')
async def tokens_refresh(token: str):
    is_expired, subject = is_refresh_token_valid(token)
    if is_expired:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    else:
        return {
            "access_token": create_access_token(subject)
        }
