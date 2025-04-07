from typing import Type
from uuid import UUID

from sqlalchemy.orm import Session

from backend.src.users import models, schemas
from backend.src.users.utils import get_hashed_password


def get_user_by_id(db: Session, user_uuid: UUID) -> models.User | None:
    return db.query(models.User).filter(models.User.uuid == user_uuid).first()


def get_user_by_username(db: Session, username: str) -> schemas.User | None:
    user = db.query(models.User).filter(models.User.username == username).first()
    return user


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[Type[schemas.User]]:
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_password = get_hashed_password(user.password)
    db_user = models.User(
        username=user.username,
        password=hashed_password,
        is_staff=user.is_staff,
        is_active=user.is_active,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(
    db: Session, user_data: schemas.UserUpdate, db_user: models.User
) -> models.User:
    if user_data.username is not None:
        db_user.username = user_data.username
    if user_data.password is not None:
        db_user.password = get_hashed_password(user_data.password)
    if user_data.is_active is not None:
        db_user.is_active = user_data.is_active
    if user_data.is_staff is not None:
        db_user.is_staff = user_data.is_staff
    if user_data.table is not None:
        db_user.table = user_data.table
    db.commit()
    db.refresh(db_user)
    return db_user
