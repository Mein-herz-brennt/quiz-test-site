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
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    status = Column(Enum)
    role = Column(Enum)
    quests = relationship('Quiz', back_populates='users')
