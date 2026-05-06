from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import User, Quiz, Question, Answer, Base
from src.settings import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)


def get_db():
    with SessionLocal() as session:
        try:
            yield session
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
