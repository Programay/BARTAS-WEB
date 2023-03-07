from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, services
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/", response_model=list[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = services.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{username}", response_model=schemas.User)
async def read_user(username: str, db: Session = Depends(get_db)):
    db_user = services.get_user_by_username(db, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/id/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = services.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/")
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> dict:
    db_user = services.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Account already exist.")
    db_user = services.create_user(db=db, user=user)
    return {"username": db_user.username}
