from typing import List
from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID, uuid4

class NoteTagLink(SQLModel, table=True):
    note_id: UUID = Field(foreign_key="note.id", primary_key=True)
    tag_id: UUID = Field(foreign_key="tag.id", primary_key=True)

class Tag(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    name: str = Field(index=True, unique=True)

    notes: List["Note"] = Relationship(back_populates="tags", link_model=NoteTagLink)