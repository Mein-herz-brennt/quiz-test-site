from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import Base

class Answears(Base):
    __tablename__ = 'answears'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey('questions.id'))
    
    question = relationship("Question", back_populates="answears", cascade='all, delete-orphan')
