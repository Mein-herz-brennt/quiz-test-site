from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import Depends
from src.core.database import get_db
from src.modules.users.models import User


class UserRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_by_username(self, username: str) -> User | None:
        return self.db.execute(select(User).where(User.username == username)).scalar_one_or_none()

    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
