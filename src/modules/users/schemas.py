from pydantic import BaseModel, ConfigDict
from src.modules.users.models import RoleEnum, StatusEnum
from datetime import datetime


class UserBase(BaseModel):
    username: str
    role: RoleEnum


class RegisterRequest(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    status: StatusEnum
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
