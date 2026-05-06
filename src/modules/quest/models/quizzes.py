from src.core.database import Base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import enum
import datetime


class QuizStatus(enum.Enum):
    draft = "draft"
    active = "active"
    deleted = "deleted"


class Quiz(Base):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    created_by = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(Enum(QuizStatus), default=QuizStatus.draft)

    user = relationship("User", back_populates="quests")
    questions = relationship("Question", back_populates="quiz", cascade='all, delete-orphan')
