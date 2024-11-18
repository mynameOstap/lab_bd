from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto


class CarImage(db.Model, IDto):
    __tablename__ = "car_img"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(512), nullable=False, unique=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    car = relationship('Car', backref='images')

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "url": self.url, "car_id": self.car_id}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]):
        return CarImage(**dto_dict)