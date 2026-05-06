import datetime
import enum
from sqlalchemy import Column, Integer, String, Enum, DateTime
from src.core.database import Base
from sqlalchemy.orm import relationship


class StatusEnum(enum.Enum):
    active = "active"
    deleted = "deleted"


class RoleEnum(enum.Enum):
    student = "Student"
    teacher = "Teacher"
    admin = "Admin"


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(Enum(StatusEnum), default=StatusEnum.active)
    role = Column(Enum(RoleEnum), default=RoleEnum.student)
    
    # Relationships
    quests = relationship('Quiz', back_populates='user')
    results = relationship('Results', back_populates='user')
