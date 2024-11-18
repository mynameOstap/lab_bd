from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Brand(db.Model, IDto):
    __tablename__ = "brand"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    country = db.Column(db.String(45), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name, "country": self.country}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]):
        return Brand(**dto_dict)