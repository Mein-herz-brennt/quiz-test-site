from src.security import verify_password
from src.models.users import User
from src.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import Depends, HTTPException, status


def get_user_by_username(username: str, db: Session) -> User | None:
    user = db.execute(select(User).where(User.username == username)).scalar_one_or_none()
    if not user:
        return None
    return user


def authenticate_user(username: str, password: str, db: Session):
    user = get_user_by_username(username, db)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user
