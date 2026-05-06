from src.security import verify_password, get_password_hash
from src.models.users import User, StatusEnum
from src.schemas.users import RegisterRequest
from sqlalchemy.orm import Session
from sqlalchemy import select


def create_user(db: Session, data: RegisterRequest) -> User:
    new_user = User(
        username=data.username,
        password=get_password_hash(data.password),
        status=StatusEnum.active,
        role=data.role,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_username(username: str, db: Session) -> User | None:
    return db.execute(select(User).where(User.username == username)).scalar_one_or_none()


def authenticate_user(username: str, password: str, db: Session) -> User | None:
    user = get_user_by_username(username, db)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user
