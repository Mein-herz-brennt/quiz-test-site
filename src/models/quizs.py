import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Enum, func
from sqlalchemy.orm import relationship

from src.models.base import Base


class Quiz(Base):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    created_by = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    status = Column(Enum)
    user = relationship('User', back_populates='quiz')
    questions = relationship("Question", back_populates="quiz")

