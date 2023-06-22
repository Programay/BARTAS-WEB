from fastapi import HTTPException, status


class InvalidCredentialException(HTTPException):
    def __init__(self):
        self.detail = "Incorrect email or password"
        self.status_code = status.HTTP_400_BAD_REQUEST


class InvalidTokenException(HTTPException):
    def __init__(self):
        self.detail = "Invalid token"
        self.status_code = status.HTTP_401_UNAUTHORIZED
