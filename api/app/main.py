from fastapi import FastAPI
from sqlmodel import SQLModel
from contextlib import asynccontextmanager
from .core.database import engine
from .api import health, users, auth, notes, tags, reminders
from .models.user import User
from .core.scheduler import scheduler

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables...")
    SQLModel.metadata.create_all(engine)

    print("Starting reminder scheduler...")
    scheduler.start()

    try:
        yield
    finally:
        print("Shutting down scheduler...")
        scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

app.include_router(health.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(notes.router)
app.include_router(tags.router)
app.include_router(reminders.router)

@app.get("/")
def root():
    return {"message": "Welcome to Recallify"}