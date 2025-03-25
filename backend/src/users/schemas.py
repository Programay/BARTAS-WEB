from uuid import UUID

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    is_active: bool = True
    is_staff: bool = False


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class User(UserBase):
    uuid: UUID
    table: str | None

    class Config:
        from_attributes = True


# Custom Response types
class UserCreateResponse(BaseModel):
    username: str


class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None
    is_active: bool | None = None
    is_staff: bool | None = None
    table: str | None = None

    class Config:
        from_attributes = True
