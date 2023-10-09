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
    id: int
    table: str

    class Config:
        from_attributes = True


# Custom Response types
class UserCreateResponse(BaseModel):
    username: str
