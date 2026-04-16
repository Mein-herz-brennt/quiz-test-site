import jwt
import datetime
from src.settings import jwt_settings
from starlette.exceptions import HTTPException
from fastapi import status


class Token:

    @staticmethod
    def _create_token(data: dict, expires_delta: datetime.timedelta, secret: str):
        to_encode = data.copy()
        to_encode.update({'exp': datetime.datetime.utcnow() + expires_delta})
        return jwt.encode(payload=to_encode, key=secret, algorithm=jwt_settings.algorithm)

    @classmethod
    def create_access_token(cls, username: str):
        return cls._create_token(
            data={"sub": username, "type": "access"},
            expires_delta=datetime.timedelta(minutes=jwt_settings.access_time_to_expire),
            secret=jwt_settings.ACCESS_SECRET_KEY
        )

    @classmethod
    def create_refresh_token(cls, username: str):
        return cls._create_token(
            data={"sub": username, "type": "refresh"},
            expires_delta=datetime.timedelta(days=jwt_settings.refresh_time_to_expire),
            secret=jwt_settings.ACCESS_SECRET_KEY
        )

    # @staticmethod
    # def get_payload(token: str, token_type: str):
    #     if token_type == 'access':
    #         secret_key = jwt_settings.ACCESS_SECRET_KEY
    #     elif token_type == 'refresh':
    #         secret_key = jwt_settings.REFRESH_SECRET_KEY
    #     else:
    #         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Token type not supported')
    #     return jwt.decode(token, secret_key, algorithms=[jwt_settings.algorithm])
    @staticmethod
    def get_payload(token: str):
        # if token_type == 'access':
        #     secret_key = jwt_settings.ACCESS_SECRET_KEY
        # elif token_type == 'refresh':
        #     secret_key = jwt_settings.REFRESH_SECRET_KEY
        # else:
        #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Token type not supported')
        data = jwt.decode(token, jwt_settings.ACCESS_SECRET_KEY, algorithms=[jwt_settings.algorithm])
        if not data:
            return None
        return data



jwt_token = Token()
