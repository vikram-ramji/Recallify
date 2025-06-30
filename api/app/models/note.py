from typing import List
from sqlmodel import Relationship, SQLModel, Field
from uuid import UUID, uuid4
from datetime import datetime, timezone
from .tag import Tag, NoteTagLink
from .reminder import Reminder

class Note(SQLModel, table=True) :
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    title: str
    content: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    user_id: UUID = Field(foreign_key="user.id")
    tags: List[Tag] = Relationship(back_populates="notes", link_model=NoteTagLink)
    reminders: List[Reminder] = Relationship(back_populates="note")