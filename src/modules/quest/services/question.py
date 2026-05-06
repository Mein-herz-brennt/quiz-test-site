from fastapi import Depends, HTTPException, status
from typing import Sequence
from src.modules.quest.repositories import QuestionRepository
from src.modules.quest.models import Question


class QuestionService:
    def __init__(
            self,
            question_repository: QuestionRepository = Depends(QuestionRepository),
    ) -> None:
        self.question_repository = question_repository

    def get_question_by_id(self, question_id: int) -> Question:
        question = self.question_repository.get_by_id(question_id)
        if question is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Question with id {question_id} not found"
            )
        return question

    def get_questions_by_quiz(self, quiz_id: int) -> Sequence[Question]:
        return self.question_repository.get_by_quiz(quiz_id)

    def delete_question(self, question_id: int) -> None:
        question = self.get_question_by_id(question_id)
        self.question_repository.delete(question)
