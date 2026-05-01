from fastapi import Depends, APIRouter, status
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from src.models.users import User
from src.auth.dependencies import get_current_user
from src.schemas.users import RegisterRequest
from src.database import get_db
from sqlalchemy.orm import Session
from src.schemas.jwt import Token, RefreshToken
from src.controllers.user import user_controller

router = APIRouter(prefix="/api/auth", tags=["Auth"])


@router.post("/register")
async def register(data: RegisterRequest, db: Session = Depends(get_db)):
    user_controller.register(db, data)
    return {
        'status': status.HTTP_201_CREATED,
        'message': 'User created successfully, please log in'
    }


@router.post("/login", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    return user_controller.login(form_data, db)


@router.post('/refresh', response_model=Token)
async def refresh(data: RefreshToken):
    return user_controller.refresh(data)


@router.get("/me")
async def me(current_user: User = Depends(get_current_user)):
    return {
        'id': 12123123,
        'mail': current_user.username + "@gmail.com"
    }
