import datetime
import enum

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from src.models.base import Base


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
    created_at = Column(datetime.time, add_now=True)
    status = Column(Enum)
    role = Column(Enum)
