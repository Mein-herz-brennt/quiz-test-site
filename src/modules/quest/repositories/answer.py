from typing import Sequence
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import Depends
from src.core.database import get_db
from src.modules.quest.models.answers import Answer
from src.modules.quest.repositories.base import BaseRepository


class AnswerRepository(BaseRepository[Answer]):
    def __init__(self, db: Session = Depends(get_db)):
        super().__init__(model=Answer, db=db)

    def get_by_question(self, question_id: int) -> Sequence[Answer]:
        return self.db.execute(
            select(Answer).where(Answer.question_id == question_id)
        ).scalars().all()

    def get_correct_by_question(self, question_id: int) -> Sequence[Answer]:
        return self.db.execute(
            select(Answer).where(
                Answer.question_id == question_id,
                Answer.is_correct == True
            )
        ).scalars().all()
