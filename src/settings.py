from decouple import config, Csv
from datetime import timedelta


class JWTConfig:
    ACCESS_SECRET_KEY: str = config('ACCESS_SECRET_KEY')
    REFRESH_SECRET_KEY: str = config('REFRESH_SECRET_KEY')
    _ACCESS_TIME_TO_EXPIRE: int = 30  # in minutes
    _REFRESH_TIME_TO_EXPIRE: int = 7  # in days
    _ALGORITHM: str = 'HS256'

    @property
    def access_time_to_expire(self):
        return self._ACCESS_TIME_TO_EXPIRE

    @access_time_to_expire.setter
    def access_time_to_expire(self, value: int):
        """TAKE TIME IN MINUTES"""
        if value:
            self._ACCESS_TIME_TO_EXPIRE = value

    @property
    def refresh_time_to_expire(self):
        return self._REFRESH_TIME_TO_EXPIRE

    @refresh_time_to_expire.setter
    def refresh_time_to_expire(self, value: int):
        """TAKE TIME IN DAYS"""
        if value:
            self._REFRESH_TIME_TO_EXPIRE = value

    @property
    def algorithm(self):
        """Crypto algorythm for coding jwt data \n
            default: HS256"""
        return self._ALGORITHM

    @algorithm.setter
    def algorithm(self, value: str):
        if value:
            self._ALGORITHM = value


class Settings:
    DATABASE_URL = config('DATABASE_URL', default='sqlite:///./quiz.db')
    HOST = config('HOST', cast=Csv(), default='localhost,127.0.0.1')
    PORT = config('PORT', default=8080)
    DATABASE = config('DATABASE', cast=str, default='sqlite:///db.sqlite3')


settings = Settings()
jwt_settings = JWTConfig()
