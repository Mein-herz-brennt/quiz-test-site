from decouple import config, Csv


class Settings:
    HOST = config('HOST', cast=Csv(), default='localhost,127.0.0.1')
    PORT = config('PORT', default=8080)
    DATABASE = config('DATABASE', cast=str, default='sqlite:///db.sqlite3')


settings = Settings()
