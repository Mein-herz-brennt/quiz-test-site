import jwt
import datetime
from src.settings import jwt_settings


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

    @staticmethod
    def get_payload(token: str):
        return jwt.decode(token, jwt_settings.ACCESS_SECRET_KEY, algorithms=[jwt_settings.algorithm])


if __name__ == '__main__':
    token = Token()
    print(jwt_token := token.create_access_token(username="test"))
    print(token.get_payload(jwt_token))