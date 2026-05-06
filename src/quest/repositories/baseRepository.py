from typing import Optional, Sequence, Type, Generic
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import Depends
from src.database import get_db
from src.quest.repositories.abstractRepository import AbstractRepository, ModelType


class BaseRepository(AbstractRepository, Generic[ModelType]):
    def __init__(self, model: ModelType, db: Session = Depends(get_db)):
        super().__init__(db)
        self.model = model

    def create(self, instance: ModelType) -> Optional[ModelType]:
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def create_all(self, instances: list[ModelType]) -> list[ModelType]:
        self.db.add_all(instances)
        self.db.commit()
        return instances

    def get_by_id(self, id_: int) -> Optional[ModelType]:
        instance = self.db.execute(select(self.model).where(self.model.id == id_))
        return instance.scalar_one_or_none()

    def get_with_pagination(self, per_page: int, pages: int = 1) -> Sequence[ModelType]:
        offset = (pages - 1) * per_page
        query = select(self.model).order_by(self.model.id).limit(per_page).offset(offset)
        results = self.db.execute(query).scalars().all()
        return results

    def get_all(self) -> Sequence[ModelType]:
        instances = self.db.execute(select(self.model)).scalars().all()
        return instances

    def update(self, instance: ModelType) -> Optional[ModelType]:
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def delete(self, instance: ModelType) -> Optional[ModelType]:
        self.db.delete(instance)
        self.db.commit()
        return instance
