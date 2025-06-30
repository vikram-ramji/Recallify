from pydantic import BaseModel, Field, EmailStr

class SignupBody(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=6)


class SigninBody(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)

class AuthResponse(BaseModel):
    access_token: str