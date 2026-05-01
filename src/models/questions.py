from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from src.models.base import Base
import enum


class QuestionStatus(enum.Enum):
    active = 'active'
    inactive = 'inactive'
    deleted = 'deleted'


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    quiz_id = Column(Integer, ForeignKey('quiz.id'))
    status = Column(Enum(QuestionStatus), default=QuestionStatus.active)
    quiz = relationship('Quiz', back_populates='questions')
    answears = relationship("Answears", back_populates="question")
