from apscheduler.schedulers.background import BackgroundScheduler # type: ignore
from sqlmodel import Session, select
from .database import engine
from datetime import datetime, timezone
from ..models.reminder import Reminder

scheduler = BackgroundScheduler()

def check_due_reminders():
    with Session(engine) as session:
        now = datetime.now(timezone.utc)
        stmt = select(Reminder).where(Reminder.remind_at <= now, Reminder.fired == False)
        reminders = session.exec(stmt).all()
        for reminder in reminders:
            # trigger notification
            reminder.fired = True
        session.commit()

scheduler.add_job(check_due_reminders, "interval", seconds=60) # type: ignore