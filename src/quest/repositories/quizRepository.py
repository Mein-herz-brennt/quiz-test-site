from typing import Optional, Sequence
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import Depends
from src.database import get_db
from src.models.quizzes import Quiz
from src.quest.repositories.baseRepository import BaseRepository


class QuizRepository(BaseRepository[Quiz]):
    def __init__(self, db: Session = Depends(get_db)):
        super().__init__(model=Quiz, db=db)

    def get_by_user(self, user_id: int) -> Sequence[Quiz]:
        return self.db.execute(
            select(Quiz).where(Quiz.created_by == user_id)
        ).scalars().all()
