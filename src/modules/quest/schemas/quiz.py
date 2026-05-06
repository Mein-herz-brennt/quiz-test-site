from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime
from src.modules.quest.models.quizzes import QuizStatus

class AnswerCreate(BaseModel):
    text: str
    is_correct: bool = False

class AnswerResponse(BaseModel):
    id: int
    text: str
    is_correct: bool
    question_id: int

    model_config = ConfigDict(from_attributes=True)

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

    model_config = ConfigDict(from_attributes=True)

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

    model_config = ConfigDict(from_attributes=True)
