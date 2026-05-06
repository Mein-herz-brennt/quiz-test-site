from src.core.database import Base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
import enum


class QuestionStatus(enum.Enum):
    active = "active"
    deleted = "deleted"


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    quiz_id = Column(Integer, ForeignKey('quiz.id'))
    status = Column(Enum(QuestionStatus), default=QuestionStatus.active)

    quiz = relationship("Quiz", back_populates="questions")
    answers = relationship("Answer", back_populates="question", cascade='all, delete-orphan')
