from typing import Optional, Sequence
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import Depends
from src.core.database import get_db
from src.modules.quest.models.questions import Question, QuestionStatus
from src.modules.quest.repositories.base import BaseRepository


class QuestionRepository(BaseRepository[Question]):
    def __init__(self, db: Session = Depends(get_db)):
        super().__init__(model=Question, db=db)

    def get_by_quiz(self, quiz_id: int) -> Sequence[Question]:
        return self.db.execute(
            select(Question).where(
                Question.quiz_id == quiz_id,
                Question.status != QuestionStatus.deleted
            )
        ).scalars().all()

    def delete(self, question: Question) -> Optional[Question]:
        question.status = QuestionStatus.deleted
        self.db.commit()
        self.db.refresh(question)
        return question
