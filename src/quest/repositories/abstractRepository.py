from abc import ABC, abstractmethod
from typing import TypeVar, Optional, Sequence
from src.models.base import Base
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType", bound=Base)


class AbstractRepository(ABC):
    def __init__(self, db: Session) -> None:
        self.db = db

    @abstractmethod
    def create(self, instance: ModelType) -> Optional[ModelType]: pass

    @abstractmethod
    def create_all(self, instances: list[ModelType]) -> list[ModelType]: pass

    @abstractmethod
    def get_by_id(self, id_: int) -> Optional[ModelType]: pass

    @abstractmethod
    def get_with_pagination(self, per_page: int, page: int = 1) -> Sequence[ModelType]: pass

    @abstractmethod
    def get_all(self) -> Sequence[ModelType]: pass

    @abstractmethod
    def update(self, instance: ModelType) -> Optional[ModelType]: pass

    @abstractmethod
    def delete(self, instance: ModelType) -> Optional[ModelType]: pass
