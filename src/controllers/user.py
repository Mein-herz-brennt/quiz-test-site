from typing import Annotated
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import status
from src.auth.service import jwt_token
from src.schemas.jwt import RefreshToken
from src.schemas.users import RegisterRequest
from src.users.service import get_user_by_username, create_user, authenticate_user


class UserController:
    @staticmethod
    def register(db: Session, data: RegisterRequest):
        if get_user_by_username(data.username, db):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already exists"
            )
        create_user(db, data)

    @staticmethod
    def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session):
        user = authenticate_user(form_data.username, form_data.password, db)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
        return {
            'access_token': jwt_token.create_access_token(user.username),
            'refresh_token': jwt_token.create_refresh_token(user.username)
        }

    @staticmethod
    def refresh(data: RefreshToken):
        payload = jwt_token.get_refresh_payload(data.refresh_token)

        username = payload.get("sub")
        token_type = payload.get("type")

        if not username or token_type != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )

        return {
            "access_token": jwt_token.create_access_token(username),
            "refresh_token": data.refresh_token,
        }


user_controller = UserController()