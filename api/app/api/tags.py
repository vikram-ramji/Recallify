from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List
from ..models.tag import Tag
from ..models.user import User
from ..models.note import Note
from ..schemas.tag import TagRead
from ..core.database import get_session
from ..auth.dependencies import get_current_user

router = APIRouter(prefix="/tags", tags=["tags"])

@router.get("/", response_model=List[TagRead])
def get_tags(user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    tags = session.exec(select(Tag).join(Tag.notes).where(Note.user_id == user.id).distinct()).all() #type: ignore
    return tags