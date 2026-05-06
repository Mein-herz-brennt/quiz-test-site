from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from src.core.dependencies import get_current_user
from src.modules.users.models import User
from src.modules.quest.services.quiz import QuizService
from src.modules.quest.services.result import ResultService
from src.modules.quest.schemas.quiz import QuizCreate, QuizResponse
from src.modules.quest.schemas.submission import QuizSubmission

router = APIRouter(prefix="/quests", tags=["Quests"])

@router.post("/", response_model=QuizResponse, status_code=status.HTTP_201_CREATED)
async def create_quiz(
    quiz_data: QuizCreate,
    current_user: User = Depends(get_current_user),
    quiz_service: QuizService = Depends(QuizService)
):
    return quiz_service.create_quiz(quiz_data, current_user.id)

@router.get("/", response_model=List[QuizResponse])
async def get_my_quizzes(
    current_user: User = Depends(get_current_user),
    quiz_service: QuizService = Depends(QuizService)
):
    return quiz_service.get_quizzes_by_user(current_user.id)

@router.get("/{quiz_id}", response_model=QuizResponse)
async def get_quiz(
    quiz_id: int,
    quiz_service: QuizService = Depends(QuizService)
):
    quiz = quiz_service.get_quiz_by_id(quiz_id)
    if not quiz:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found")
    return quiz

@router.post("/submit", status_code=status.HTTP_201_CREATED)
async def submit_quiz(
    submission: QuizSubmission,
    current_user: User = Depends(get_current_user),
    result_service: ResultService = Depends(ResultService)
):
    return result_service.submit_quiz(submission, current_user.id)

@router.get("/results/me")
async def get_my_results(
    current_user: User = Depends(get_current_user),
    result_service: ResultService = Depends(ResultService)
):
    return result_service.get_user_results(current_user.id)
