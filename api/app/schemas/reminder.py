from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class ReminderCreate(BaseModel):
    remind_at: datetime

class ReminderRead(BaseModel):
    id: UUID
    remind_at: datetime
    fired:bool