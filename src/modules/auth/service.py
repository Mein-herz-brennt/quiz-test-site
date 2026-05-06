import jwt
import datetime
from jwt import ExpiredSignatureError, InvalidTokenError
from src.core.config import settings
from fastapi import HTTPException, status, Depends


class TokenService:

    @staticmethod
    def _create_token(data: dict, expires_delta: datetime.timedelta, secret: str) -> str:
        to_encode = data.copy()
        to_encode.update({'exp': datetime.datetime.utcnow() + expires_delta})
        return jwt.encode(payload=to_encode, key=secret, algorithm=settings.ALGORITHM)

    @classmethod
    def create_access_token(cls, username: str) -> str:
        return cls._create_token(
            data={"sub": username, "type": "access"},
            expires_delta=datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
            secret=settings.ACCESS_SECRET_KEY
        )

    @classmethod
    def create_refresh_token(cls, username: str) -> str:
        return cls._create_token(
            data={"sub": username, "type": "refresh"},
            expires_delta=datetime.timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
            secret=settings.REFRESH_SECRET_KEY
        )

    @staticmethod
    def get_access_payload(token: str) -> dict:
        try:
            data = jwt.decode(token, settings.ACCESS_SECRET_KEY, algorithms=[settings.ALGORITHM])
        except ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
        except InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return data

    @staticmethod
    def get_refresh_payload(token: str) -> dict:
        try:
            data = jwt.decode(token, settings.REFRESH_SECRET_KEY, algorithms=[settings.ALGORITHM])
        except ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token has expired")
        except InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
        return data


from src.modules.users.services import UserService
from src.modules.auth.schemas import Token, RefreshTokenRequest


class AuthService:
    def __init__(
        self, 
        user_service: UserService = Depends(UserService),
        token_service: TokenService = Depends(lambda: jwt_token)
    ):
        self.user_service = user_service
        self.token_service = token_service

    def login(self, username: str, password: str) -> Token:
        user = self.user_service.authenticate_user(username, password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
        return Token(
            access_token=self.token_service.create_access_token(user.username),
            refresh_token=self.token_service.create_refresh_token(user.username)
        )

    def refresh(self, refresh_token: str) -> Token:
        payload = self.token_service.get_refresh_payload(refresh_token)
        username = payload.get("sub")
        token_type = payload.get("type")

        if not username or token_type != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )

        return Token(
            access_token=self.token_service.create_access_token(username),
            refresh_token=refresh_token
        )


jwt_token = TokenService()
