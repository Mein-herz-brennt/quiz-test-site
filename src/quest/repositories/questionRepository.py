from typing import Sequence
from fastapi import Depends
from src.database import get_db
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.questions import Question, QuestionStatus


class QuestionRepository:
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def create(self, question: Question) -> Question:
        self.db.add(question)
        self.db.commit()
        self.db.refresh(question)
        return question

    def get_question_by_id(self, question_id: int) -> Question | None:
        result = self.db.execute(
            select(Question)
            .where(Question.id == question_id)
        )
        return result.scalar_one_or_none()

    def get_questions_with_pagination(self, per_page: int, pages: int = 1) -> Sequence[Question]:
        offset = (pages - 1) * per_page
        query = select(Question).order_by(Question.id).limit(per_page).offset(offset)
        results = self.db.execute(query).scalars().all()
        return results

    def get_all(self) -> Sequence[Question]:
        result = self.db.scalars(select(Question))
        return result.all()

    def update(self, question: Question) -> Question | None:
        self.db.commit()
        self.db.refresh(question)
        return question

    def delete(self, question: Question) -> Question | None:
        if question.status == QuestionStatus.active:
            question.status = QuestionStatus.deleted
        self.db.commit()
        self.db.refresh(question)
        return question
