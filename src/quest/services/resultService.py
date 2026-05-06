from fastapi import Depends, HTTPException, status
from typing import List, Sequence
from src.quest.repositories.resultRepository import ResultRepository
from src.quest.repositories.answerRepository import AnswerRepository
from src.models.results import Results
from src.quest.schemas.submission import AnswerSubmission, QuizSubmission


class ResultService:
    def __init__(
            self,
            result_repository: ResultRepository = Depends(ResultRepository),
            answer_repository: AnswerRepository = Depends(AnswerRepository),
    ) -> None:
        self.result_repository = result_repository
        self.answer_repository = answer_repository

    def submit_quiz(self, submission: QuizSubmission, user_id: int) -> Results:
        score = 0
        total_questions = len(submission.submissions)
        
        if total_questions == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No answers submitted"
            )

        for sub in submission.submissions:
            answer = self.answer_repository.get_by_id(sub.answer_id)
            if answer and answer.question_id == sub.question_id and answer.is_correct:
                score += 1
        
        result = Results(
            user_id=user_id,
            quiz_id=submission.quiz_id,
            score=score
        )
        
        return self.result_repository.create(result)

    def get_user_results(self, user_id: int) -> Sequence[Results]:
        return self.result_repository.get_by_user(user_id)

    def get_quiz_results(self, quiz_id: int) -> Sequence[Results]:
        return self.result_repository.get_by_quiz(quiz_id)
