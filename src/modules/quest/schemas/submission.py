from pydantic import BaseModel
from typing import List

class AnswerSubmission(BaseModel):
    question_id: int
    answer_id: int

class QuizSubmission(BaseModel):
    quiz_id: int
    submissions: List[AnswerSubmission]
