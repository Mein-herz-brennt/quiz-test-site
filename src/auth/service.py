import jwt
import datetime
from jwt import ExpiredSignatureError, InvalidTokenError
from src.settings import jwt_settings
from fastapi import HTTPException, status


class TokenService:

    @staticmethod
    def _create_token(data: dict, expires_delta: datetime.timedelta, secret: str) -> str:
        to_encode = data.copy()
        to_encode.update({'exp': datetime.datetime.utcnow() + expires_delta})
        return jwt.encode(payload=to_encode, key=secret, algorithm=jwt_settings.algorithm)

    @classmethod
    def create_access_token(cls, username: str) -> str:
        return cls._create_token(
            data={"sub": username, "type": "access"},
            expires_delta=datetime.timedelta(minutes=jwt_settings.access_time_to_expire),
            secret=jwt_settings.ACCESS_SECRET_KEY
        )

    @classmethod
    def create_refresh_token(cls, username: str) -> str:
        return cls._create_token(
            data={"sub": username, "type": "refresh"},
            expires_delta=datetime.timedelta(days=jwt_settings.refresh_time_to_expire),
            secret=jwt_settings.REFRESH_SECRET_KEY
        )

    @staticmethod
    def get_access_payload(token: str) -> dict:
        try:
            data = jwt.decode(token, jwt_settings.ACCESS_SECRET_KEY, algorithms=[jwt_settings.algorithm])
        except ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
        except InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return data

    @staticmethod
    def get_refresh_payload(token: str) -> dict:
        try:
            data = jwt.decode(token, jwt_settings.REFRESH_SECRET_KEY, algorithms=[jwt_settings.algorithm])
        except ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token has expired")
        except InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
        return data


jwt_token = TokenService()
