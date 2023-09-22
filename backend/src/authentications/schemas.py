from pydantic import BaseModel


# Custom Response types
class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str


class RefreshLoginResponse(BaseModel):
    access_token: str
