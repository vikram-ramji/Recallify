from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timezone
import uuid

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    password: str = Field(min_length=6)
    auth_provider: Optional[str] = Field(default="email")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))