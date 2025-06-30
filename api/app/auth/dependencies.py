from fastapi import Depends, HTTPException, Header
from sqlmodel import Session
from ..auth.jwt import decode_token
from ..core.database import get_session
from ..models.user import User

def get_current_user(
    authorization: str = Header(..., alias="Authorization"),
    session: Session = Depends(get_session)
) -> User:
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")

    token = authorization.split(" ")[1]

    try:
        payload = decode_token(token)
        user_id = payload.get("sub")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
