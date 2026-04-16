from fastapi import Depends, APIRouter
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from src.models.users import User
from src.auth.dependencies import get_current_user

router = APIRouter(prefix="/api/auth")


@router.post("/login", response_model=...)
async def login(oauth_form: OAuth2PasswordRequestForm = Depends(),
                user=...):
    ...


@router.post('/refresh')
async def refresh():
    ...


@router.get("/me")
async def me(current_user: User = Depends(get_current_user)):
    return {
        'id': 12123123,
        'mail': current_user.username + "@gmail.com"
    }
