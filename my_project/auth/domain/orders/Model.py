from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import backref

from my_project import db
from my_project.auth.domain.i_dto import IDto

from sqlalchemy.orm import relationship
from my_project import db

class Model(db.Model, IDto):
    __tablename__ = "model"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body_type = db.Column(db.Enum("sedan", "hatchback", "suv", "coupe"), nullable=False)
    engine_id = db.Column(db.Integer, db.ForeignKey('engine.id'), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    engine = relationship('Engine', backref='models')
    brand = relationship('Brand', backref='models')

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "body_type": self.body_type, "engine_id": self.engine_id, "brand_id": self.brand_id}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]):
        return Model(**dto_dict)
