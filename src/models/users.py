import datetime
import enum
from sqlalchemy import Column, Integer, String, Enum, DateTime
from src.models.base import Base
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
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(Enum(StatusEnum))
    role = Column(Enum(RoleEnum))
    quests = relationship('Quiz', back_populates='user')
