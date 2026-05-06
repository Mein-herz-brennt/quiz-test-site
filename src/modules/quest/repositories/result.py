from typing import Sequence, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import Depends
from src.core.database import get_db
from src.modules.quest.models.results import Results
from src.modules.quest.repositories.base import BaseRepository


class ResultRepository(BaseRepository[Results]):
    def __init__(self, db: Session = Depends(get_db)):
        super().__init__(model=Results, db=db)

    def get_by_user(self, user_id: int) -> Sequence[Results]:
        return self.db.execute(
            select(Results).where(Results.user_id == user_id)
        ).scalars().all()

    def get_by_quiz(self, quiz_id: int) -> Sequence[Results]:
        return self.db.execute(
            select(Results)
            .where(Results.quiz_id == quiz_id)
            .order_by(Results.score.desc())
        ).scalars().all()

    def get_by_user_and_quiz(self, user_id: int, quiz_id: int) -> Optional[Results]:
        return self.db.execute(
            select(Results).where(
                Results.user_id == user_id,
                Results.quiz_id == quiz_id
            )
        ).scalar_one_or_none()
