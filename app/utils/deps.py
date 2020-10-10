from typing import Generator
from app.db.session import SessionLocal


def get_db():
    try:
        db = SessionLocal()
        return db
    finally:
        db.close()
