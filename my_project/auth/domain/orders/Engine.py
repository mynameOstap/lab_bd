from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Engine(db.Model, IDto):
    __tablename__ = "engine"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    eng_vol = db.Column(db.Float, nullable=False)
    hp = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    brand = relationship('Brand', backref='engines')

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "eng_vol": self.eng_vol, "hp": self.hp, "name": self.name, "brand_id": self.brand_id}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]):
        return Engine(**dto_dict)
