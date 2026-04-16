from datetime import datetime, timezone
from typing import Annotated
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import status
from src.auth.service import jwt_token
from src.models import User
from src.models.users import StatusEnum
from src.schemas.jwt import RefreshToken
from src.schemas.users import RegisterRequest
from src.security import get_password_hash
from src.users.service import get_user_by_username, register_user, authenticate_user


class UserController:
    @staticmethod
    def register(db: Session, data: RegisterRequest):
        if get_user_by_username(data.username, db):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="User already exists")

        new_user = User(
            username=data.username,
            password=get_password_hash(data.password),
            status=StatusEnum.active,
            role=data.role,
        )
        register_user(db, new_user)

    @staticmethod
    def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session):
        user = authenticate_user(form_data.username, form_data.password, db)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="incorrect username or password")

        return {
            'access_token': jwt_token.create_access_token(user.username),
            'refresh_token': jwt_token.create_refresh_token(user.username)
        }

    @staticmethod
    def refresh(data: RefreshToken):
        payload = jwt_token.get_payload(data.refresh_token)
        username = payload.get("sub")
        token_type = payload.get("type")
        expires_in = payload.get("exp")

        if username is None or token_type != "refresh":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

        if expires_in < datetime.now(timezone.utc):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Expired token")

        access_token = jwt_token.create_access_token(username)

        return {
            "access_token": access_token,
            "refresh_token": data.refresh_token,
        }


user_controller = UserController()