from typing import List
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from .tag import TagRead

class NoteCreate(BaseModel):
    title: str
    content: str
    tag_names: List[str] = []

class NoteRead(BaseModel):
    id: UUID
    title: str
    content: str
    created_at: datetime
    tags: List[TagRead]