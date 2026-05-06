from fastapi import APIRouter, Depends, status
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from src.modules.users.services import UserService
from src.modules.users.schemas import RegisterRequest
from src.modules.auth.schemas import Token, RefreshTokenRequest
from src.modules.auth.service import AuthService
from src.core.dependencies import get_current_user
from src.modules.users.models import User

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    data: RegisterRequest, 
    user_service: UserService = Depends(UserService)
):
    user_service.create_user(data)
    return {
        'status': status.HTTP_201_CREATED,
        'message': 'User created successfully, please log in'
    }


@router.post("/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], 
    auth_service: AuthService = Depends(AuthService)
):
    return auth_service.login(form_data.username, form_data.password)


@router.post('/refresh', response_model=Token)
async def refresh(
    data: RefreshTokenRequest,
    auth_service: AuthService = Depends(AuthService)
):
    return auth_service.refresh(data.refresh_token)


@router.get("/me")
async def me(current_user: User = Depends(get_current_user)):
    return {
        'id': current_user.id,
        'username': current_user.username,
        'role': current_user.role,
        'status': current_user.status,
    }
