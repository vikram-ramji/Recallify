from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query
from ..schemas.note import NoteCreate, NoteRead
from typing import List, Set
from ..models.user import User
from ..auth.dependencies import get_current_user
from ..models.note import Note
from sqlmodel import Session, func, select
from sqlalchemy.orm import selectinload
from ..core.database import get_session
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timezone
from ..models.tag import Tag
from ..schemas.reminder import ReminderCreate, ReminderRead
from ..models.reminder import Reminder

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("/", response_model=NoteRead)
def create_note(data: NoteCreate, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    try:
        tags: List[Tag] = []
        seen_names: Set[str] = set()
        for name in data.tag_names:
            name = name.strip().lower()
            if name in seen_names:
                continue
            seen_names.add(name)

            tag = session.exec(select(Tag).where(func.lower(Tag.name) == name.lower())).first()
            if not tag:
                tag = Tag(name=name)
                session.add(tag)
            tags.append(tag)

        note = Note(title=data.title, content=data.content, user_id=user.id, tags=tags)
        
        session.add(note)
        session.commit()
        session.refresh(note)
        return note
    except SQLAlchemyError as exc:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(exc)}")


@router.get("/", response_model=List[NoteRead])
def list_notes(
    user: User = Depends(get_current_user), 
    session: Session = Depends(get_session), 
    offset: int = 0, 
    limit: int = 10,
    tag: List[str] = Query(None)
    ):
    try:
        stmt = (
            select(Note)
            .options(selectinload(Note.tags)) # type: ignore
            .where(Note.user_id == user.id)
        )

        if tag:
            tag_names = [t.strip().lower() for t in tag]
            stmt = (
                stmt.join(Note.tags)  # type: ignore
                .where(func.lower(Tag.name).in_(tag_names))
                .distinct()
            )

        notes = session.exec(stmt.offset(offset).limit(limit)).all()
        return notes

    except SQLAlchemyError as exc:
        raise HTTPException(status_code=500, detail=f"Query error: {str(exc)}")

@router.get("/{note_id}", response_model=NoteRead)
def get_note(note_id: UUID, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if not note or note.user_id != user.id:
        raise HTTPException(400, "Note not found")
    return note

@router.put("/{note_id}", response_model=NoteRead)
def update_note(note_id: UUID, data: NoteCreate, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if not note or note.user_id != user.id:
        raise HTTPException(400, "Note not found")
    note.title = data.title
    note.content = data.content
    note.updated_at = datetime.now(timezone.utc)

    session.add(note)
    session.commit()
    session.refresh(note)

    return note

@router.delete("/{note_id}", status_code=204)
def delete_note(note_id: UUID, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if not note or note.user_id != user.id:
        raise HTTPException(400, "Note not found")

    session.delete(note)
    session.commit()

@router.post("/{note_id}/reminder", response_model=ReminderRead)
def create_reminder(note_id: UUID, data: ReminderCreate, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if not note or note.user_id != user.id:
        raise HTTPException(400, "Note not found")
    
    reminder = Reminder(note_id=note_id, remind_at=data.remind_at)

    session.add(reminder)
    session.commit()
    session.refresh(reminder)
    return reminder

@router.get("/{note_id}/reminders", response_model=List[ReminderRead])
def get_reminders(note_id: UUID, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if not note or note.user_id != user.id:
        raise HTTPException(400, "Note not found")
    
    return note.reminders