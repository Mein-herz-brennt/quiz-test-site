import enum
from sqlalchemy import Column, Integer, String, Enum, DateTime
from src.database import Base
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
    created_at = Column(DateTime, add_now=True)
    status = Column(Enum)
    role = Column(Enum)
    quests = relationship('Quiz', back_populates='users')
