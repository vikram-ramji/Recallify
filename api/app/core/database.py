import os
from sqlmodel import create_engine, Session

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://recall:recall@db:5432/recallify")

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    return Session(engine)