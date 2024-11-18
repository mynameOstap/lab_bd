from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto



class Car(db.Model, IDto):
    __tablename__ = "car"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    damage = db.Column(db.Enum("cosmetic_damage", "severely_damaged",
                               "moderately_damaged", "excellent_condition"), nullable=False)
    test_drive_id = db.Column(db.Integer, db.ForeignKey('test_drive.id'), nullable=True)
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    test_drive = db.relationship('TestDrive', backref='cars')
    model = db.relationship('Model', backref='cars')
    seller = db.relationship('Seller', backref='cars')

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "damage": self.damage,
            "price": self.price,
            "test_drive": self.test_drive.put_into_dto() if self.test_drive else None,
            "model": self.model.put_into_dto() if self.model else None,
            "seller": self.seller.put_into_dto() if self.seller else None,
        }
