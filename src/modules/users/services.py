from fastapi import Depends, HTTPException, status
from src.core.security import verify_password, get_password_hash
from src.modules.users.models import User, StatusEnum
from src.modules.users.schemas import RegisterRequest
from src.modules.users.repositories import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository = Depends(UserRepository)):
        self.user_repo = user_repo

    def create_user(self, data: RegisterRequest) -> User:
        if self.user_repo.get_by_username(data.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered"
            )
        
        new_user = User(
            username=data.username,
            password=get_password_hash(data.password),
            status=StatusEnum.active,
            role=data.role,
        )
        return self.user_repo.create(new_user)

    def get_user_by_username(self, username: str) -> User | None:
        return self.user_repo.get_by_username(username)

    def authenticate_user(self, username: str, password: str) -> User | None:
        user = self.get_user_by_username(username)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user
