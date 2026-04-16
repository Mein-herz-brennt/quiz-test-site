from pydantic import BaseModel
from src.models.users import RoleEnum

class RegisterRequest(BaseModel):
    username: str
    password: str
    role: RoleEnum