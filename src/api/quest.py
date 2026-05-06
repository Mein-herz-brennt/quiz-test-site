from fastapi import APIRouter, Depends, status
from typing import List
from src.auth.dependencies import get_current_user
from src.models.users import User
from src.quest.services.quizService import QuizService
from src.quest.services.resultService import ResultService
from src.quest.schemas import QuizCreate, QuizResponse, QuizSubmission
from src.models.results import Results as ResultModel # Alias to avoid confusion with ResultService return types if needed

router = APIRouter(prefix="/api/quests", tags=["Quests"])

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
        from fastapi import HTTPException
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
