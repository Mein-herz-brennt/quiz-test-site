from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from src.models.base import Base


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    quiz_id = Column(Integer, ForeignKey('quiz.id'))
    status = Column(Enum)
    quiz = relationship('Quiz', back_populates='questions')
