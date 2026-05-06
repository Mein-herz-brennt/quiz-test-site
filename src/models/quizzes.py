import datetime
import enum
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship

from src.models.base import Base


class QuizStatus(enum.Enum):
    draft = "draft"
    published = "published"
    archived = "archived"


class Quiz(Base):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    created_by = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    status = Column(Enum(QuizStatus), default=QuizStatus.draft)
    user = relationship('User', back_populates='quests')
    questions = relationship("Question", back_populates="quiz", cascade='all, delete-orphan')

