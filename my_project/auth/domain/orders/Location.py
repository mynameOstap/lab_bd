from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Location(db.Model, IDto):
    __tablename__ = "location"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(45), nullable=False)
    city = db.Column(db.String(45), nullable=False)
    street = db.Column(db.String(45), nullable=False)
    building = db.Column(db.String(45), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "country": self.country, "city": self.city, "street": self.street, "building": self.building}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]):
        return Location(**dto_dict)