from ..core.celery import celery_app
from time import sleep

@celery_app.task(name="app.tasks.send_reminder_email")
def send_reminder_email(user_email: str, note_title: str):
    print(f"[📨] Sending reminder to {user_email} about: {note_title}")
    sleep(2)  # simulate network delay
    print(f"[✅] Email sent to {user_email}")