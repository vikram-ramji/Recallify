from passlib.context import CryptContext
from fastapi import Response

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def set_refresh_cookie(response: Response, token: str):
    response.set_cookie(
        key="refresh_token",
        value=token,
        max_age= 60 * 60 * 24 * 7 ,
        httponly=True,
        secure=True,
        samesite="lax"
    )