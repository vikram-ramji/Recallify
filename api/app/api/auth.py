from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import JSONResponse
from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from ..auth.jwt import decode_token, create_access_token, create_refresh_token
from ..auth.utils import hash_password, verify_password, set_refresh_cookie
from ..core.database import get_session
from ..models.user import User
from ..schemas.auth import AuthResponse, SignupBody, SigninBody


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup", response_model=AuthResponse, status_code=201)
def signup(data: SignupBody,session: Session = Depends(get_session)):
    existing_user = session.exec(select(User).where(User.email == data.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists!")
    user = User(
        username=data.username,
        password=hash_password(data.password),
        email=data.email,
        auth_provider="email"
        )
    try:
        session.add(user)
        session.commit()
        session.refresh(user)
        access_token= create_access_token({"sub": str(user.id)})
        refresh_token = create_refresh_token({"sub": str(user.id)})
        response = JSONResponse(content={"access_token": access_token})
        set_refresh_cookie(response, refresh_token)
        return response
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=400, detail="Integrity constraint violated — duplicate email or username")
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(status_code=500, detail="Unexpected database error")


@router.post("/signin", response_model=AuthResponse, status_code=201)
def signin(data: SigninBody, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.email == data.email)).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=422, detail="Invalid Credentials")
    access_token= create_access_token({"sub": str(user.id)})
    refresh_token = create_refresh_token({"sub": str(user.id)})
    response = JSONResponse(content={"access_token": access_token})
    set_refresh_cookie(response, refresh_token)
    return response


@router.post("/refresh", response_model=AuthResponse)
def refresh_token(request: Request):
    token = request.cookies.get("refresh_token")
    if not token:
        raise HTTPException(status_code=401, detail="Refresh token missing")

    try:
        payload = decode_token(token)
        user_id = payload.get("sub")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")

    new_token = create_access_token({"sub": user_id})
    return {"access_token": new_token}
