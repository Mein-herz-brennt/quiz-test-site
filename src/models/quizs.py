import enum

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.database import Base


class Quiz(Base):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    created_by = Column(Integer, ForeignKey('user.id'))
    created_at = Column(DateTime, add_now=True)
    status = Column(enum.Enum)
    user = relationship('User', back_populates='quiz')
    questions = relationship("Question", back_populates="quiz")

