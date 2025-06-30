from fastapi import APIRouter
from ..tasks.reminder import send_reminder_email

router = APIRouter(prefix="/reminders", tags=["Reminders"])

@router.post("/test")
def trigger_test_email():
    send_reminder_email.delay("demo@user.com", "Write your next chapter")
    return {"message": "Task sent to queue!"}
