from fastapi import Depends, APIRouter, HTTPException, status
from src.auth.service import jwt_token
from fastapi.security import OAuth2PasswordRequestForm
from src.models.users import User
from src.auth.dependencies import get_current_user
from src.users.service import authenticate_user, get_user_by_username
from src.schemas.users import RegisterRequest
from src.database import get_db
from sqlalchemy.orm import Session
from src.security import get_password_hash
from src.schemas.jwt import Token, RefreshToken

router = APIRouter(prefix="/api/auth")


def register_user(db, user):
    db.add(user)


@router.post("/register")
async def register(data: RegisterRequest, db: Session = Depends(get_db)):

    if get_user_by_username(data.username, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="User already exists")



    new_user = User(
        username=data.username,
        password=get_password_hash(data.password)
    )
    register_user(db, new_user)
    return {
        'status': status.HTTP_201_CREATED,
        'message': 'User created successfully, please log in'
    }


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="incorrect username or password")

    return {
        'access_token': jwt_token.create_access_token(user.username),
        'refresh_token': jwt_token.create_refresh_token(user.username)
    }


@router.post('/refresh', response_model=Token)
async def refresh(data: RefreshToken):
    payload = jwt_token.get_payload(data.access_token)
    username = payload.get("sub")
    token_type = payload.get("type")

    if username is None or token_type != "refresh":
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    access_token = jwt_token.create_access_token(username)
    refresh_token = jwt_token.create_refresh_token(username)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }


@router.get("/me")
async def me(current_user: User = Depends(get_current_user)):
    return {
        'id': 12123123,
        'mail': current_user.username + "@gmail.com"
    }
