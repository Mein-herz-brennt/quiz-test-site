from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from src.models.quizzes import QuizStatus


class AnswerCreate(BaseModel):
    text: str
    is_correct: bool = False


class AnswerResponse(BaseModel):
    id: int
    text: str
    is_correct: bool
    question_id: int

    class Config:
        from_attributes = True


class QuestionCreate(BaseModel):
    title: str
    description: Optional[str] = None
    answers: List[AnswerCreate]


class QuestionResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    quiz_id: int
    answers: List[AnswerResponse]

    class Config:
        from_attributes = True


class QuizCreate(BaseModel):
    title: str
    questions: List[QuestionCreate]


class QuizResponse(BaseModel):
    id: int
    title: str
    created_by: int
    created_at: datetime
    status: QuizStatus
    questions: List[QuestionResponse]

    class Config:
        from_attributes = True
