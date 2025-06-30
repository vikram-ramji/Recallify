from jwt import encode, decode, ExpiredSignatureError, PyJWTError # type: ignore
import os
from dotenv import load_dotenv
from typing import Any
from datetime import timedelta, datetime, timezone

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
ALGORITHM = "HS256"
ENV = os.getenv("ENV", "dev")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7))

def create_access_token(data: dict[str, Any]) -> str:
    return _create_token(data, minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

def create_refresh_token(data: dict[str, Any]) -> str:
    return _create_token(data, days=REFRESH_TOKEN_EXPIRE_DAYS)

def _create_token(data: dict[str, Any], minutes: int = 0, days: int = 0) -> str:
    encode_data = data.copy()
    if ENV != "dev":
        expire = datetime.now(timezone.utc) + timedelta(minutes=minutes, days=days)
        encode_data.update({"exp": expire})
    return encode(encode_data, SECRET_KEY, ALGORITHM)

def decode_token(token: str) -> dict[str, Any]:
    try:
        return decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except ExpiredSignatureError:
        raise ValueError("Token expired!")
    except PyJWTError:
        raise ValueError("Invalid token")